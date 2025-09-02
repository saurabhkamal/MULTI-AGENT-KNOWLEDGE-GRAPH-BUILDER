import requests

WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

def search_wikipedia(query):
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": query
    }

    headers = {
        "User-Agent": "MyWikipediaBot/1.0 (https://yourdomain.com)"  # 👈 Add a User-Agent
    }

    response = requests.get(WIKI_API_URL, params=params, headers=headers)

    # --- Debug: Check what comes back ---
    if response.status_code != 200:
        raise Exception(f"API returned {response.status_code}: {response.text[:200]}")

    try:
        data = response.json()
    except ValueError:
        raise Exception(f"Response not JSON. Got: {response.text[:200]}")

    # Handle missing keys safely
    if "query" not in data or "pages" not in data["query"]:
        return ""

    page = next(iter(data["query"]["pages"].values()))
    return page.get("extract", "")
