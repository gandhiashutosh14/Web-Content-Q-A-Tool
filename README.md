# Web Content Q&A Tool

This tool allows users to input URLs, extract their content, and ask questions about the information contained within those pages. The tool provides answers based solely on the content from the provided URLs, without relying on external knowledge.

## Features

- URL content ingestion
- Text-based question answering
- Source attribution for answers
- Relevance scoring
- Clean and intuitive user interface

## Requirements

- Python 3.8+
- Required packages listed in `requirements.txt`

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd web-content-qa
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your default web browser.

## Usage

1. Enter a URL in the input field and click "Add URL" to analyze its content
2. Add multiple URLs as needed
3. Enter your question in the question input field
4. Click "Get Answer" to receive relevant information from the analyzed content

## How it Works

1. **Content Ingestion**:
   - URLs are processed using BeautifulSoup for HTML parsing
   - Text content is extracted and cleaned
   - Content is split into sentences for granular analysis

2. **Question Answering**:
   - Uses TF-IDF vectorization for text representation
   - Employs cosine similarity for finding relevant content
   - Returns multiple relevant passages with source attribution

3. **Results**:
   - Displays relevant text passages
   - Shows source URLs
   - Includes relevance scores for transparency

## Limitations

- Only processes text content (no images or other media)
- Requires active internet connection for URL fetching
- Basic text similarity matching (no advanced NLP or deep learning)
- Memory-based storage (content is lost when the application restarts)

## Future Improvements

- Add support for PDF and other document types
- Implement persistent storage
- Add more advanced NLP techniques
- Improve answer generation and summarization
- Add support for authentication and user sessions