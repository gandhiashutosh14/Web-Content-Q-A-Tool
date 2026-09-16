# Web Content Q&A — Historical Retrieval Baseline

> **Status:** historical prototype; not part of my current recruiter-facing portfolio.

This small Streamlit project explores a pre-LLM retrieval baseline: ingest text from user-supplied web pages, represent passages with TF-IDF, rank them with cosine similarity, and show the most relevant excerpts with source URLs.

It is intentionally simple and is useful mainly as a historical contrast with the retrieval, grounding, evaluation, and agentic systems in my newer work.

## What it demonstrates

- URL ingestion and HTML text extraction with BeautifulSoup.
- TF-IDF representation and cosine-similarity retrieval.
- Source attribution and relevance scores.
- A lightweight Streamlit interface.

## Run locally

```bash
git clone https://github.com/gandhiashutosh14/Web-Content-Q-A-Tool.git
cd Web-Content-Q-A-Tool
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Scope

This is **not RAG and not a production Q&A system**: there is no embedding model, generative model, persistent store, authentication, or retrieval evaluation set. It is retained as an earlier information-retrieval exercise rather than actively maintained.

For current work, start from my [GitHub profile](https://github.com/gandhiashutosh14).
