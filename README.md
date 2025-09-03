# Building a Multi-Agent Knowledge Graph Builder with LangGraph, Streamlit, and AI

### Introduction
In today's information-driven world, structuring knowledge is just as important as generating it. Researchers, companies, and learners often struggle with scattered information that lacks context. To solve this, I built a Multi-Agent Knowledge Graph Builder — an AI-powered system that generates interactive mind maps and learning roadmaps from just a single user query.

This project combines:
- LangGraph – for building intelligent multi-agent workflows
- Streamlit – to create an interactive web application
- Graphviz & PIL – for graph visualization
- Autonomous Pipelines – for fully automated knowledge generation

By integrating these tools, I created a platform where anyone can enter a topic (e.g., “Roadmap for Machine Learning”) and instantly get a visualized knowledge map — structured, downloadable, and ready to use.

### How It Works – Step by Step
1. Multi-Agent Orchestration with LangGraph: I used LangGraph to define how different AI agents interact:

graph.add_node("research", wrapped_researcher)<br>
graph.add_node("synthesize", wrapped_synthesizer)<br>
graph.add_node("map", wrapped_mapper)

Each agent has a role:
- Researcher – Finds information about the topic
- Synthesizer – Summarizes and refines the knowledge
- Mapper – Builds logical connections between concepts

Think of it as a team of AI assistants, each specializing in a step of the process.

2. Autonomous Pipeline for End-to-End Flow

<img width="1501" height="202" alt="image" src="https://github.com/user-attachments/assets/3b379086-44a0-4c11-a05d-1c7069495b39" />

- The user enters a topic.
- The pipeline calls LangGraph.
- A knowledge graph structure is returned.

This ensures that the process is fully automated — no manual intervention required.

3. Streamlit App for User Interaction
- Users type in a question or topic.
- The app shows a loading spinner while the graph is being generated.
- A visual knowledge map is displayed instantly.

4. Knowledge Graph Visualization
- The graph is exported using Graphviz and displayed as an SVG image.
- Example (for “Machine Learning”):
  - Machine Learning → Supervised Learning → Regression, Classification
  - Machine Learning → Unsupervised Learning → Clustering, Dimensionality Reduction
 
5. Downloadable Insights
- This ensures knowledge maps are not just for viewing, but also reusable in research papers, presentations, or strategy decks.

This project demonstrates how AI + visualization + user-friendly design can transform abstract knowledge into tangible, structured insights.


<img width="2393" height="650" alt="image" src="https://github.com/user-attachments/assets/5bf8abc7-2e05-4a2f-843f-d4ed83b5ff8b" />

<img width="2354" height="1121" alt="image" src="https://github.com/user-attachments/assets/dadf62e7-9181-4184-b663-ecec49360470" />

<img width="2518" height="561" alt="image" src="https://github.com/user-attachments/assets/101b2aa3-614c-4dff-b3ab-1e34fea37cf3" />

<img width="2522" height="591" alt="image" src="https://github.com/user-attachments/assets/e77613fc-e58f-490a-9677-cea90999178d" />

<img width="2540" height="606" alt="image" src="https://github.com/user-attachments/assets/099a1b0e-1507-4cc3-b87d-80c4ec62d1be" />






