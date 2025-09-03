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

graph.add_node("research", wrapped_researcher)
graph.add_node("synthesize", wrapped_synthesizer)
graph.add_node("map", wrapped_mapper)
