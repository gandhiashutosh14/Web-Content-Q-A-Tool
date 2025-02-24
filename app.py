import streamlit as st
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

class ContentStore:
    def __init__(self):
        self.documents = []
        self.urls = []
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None
        
    def add_content(self, url, content):
        # Split content into sentences
        sentences = sent_tokenize(content)
        # Add source URL to each sentence
        self.documents.extend(sentences)
        self.urls.extend([url] * len(sentences))
        # Update TF-IDF matrix
        self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)
    
    def find_relevant_content(self, query, top_k=3):
        if not self.documents:
            return []
        
        # Transform query
        query_vector = self.vectorizer.transform([query])
        
        # Calculate similarity
        similarities = cosine_similarity(query_vector, self.tfidf_matrix)[0]
        
        # Get top matches
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0:  # Only include relevant matches
                results.append({
                    'text': self.documents[idx],
                    'url': self.urls[idx],
                    'score': similarities[idx]
                })
        
        return results

def fetch_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
            
        # Get text content
        text = soup.get_text()
        
        # Clean up text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text
    except Exception as e:
        st.error(f"Error fetching content from {url}: {str(e)}")
        return None

# Initialize session state
if 'content_store' not in st.session_state:
    st.session_state.content_store = ContentStore()

# App UI
st.title("Web Content Q&A Tool")
st.write("Enter URLs to analyze and ask questions about their content.")

# URL input
url_input = st.text_input("Enter a URL to analyze:")
if st.button("Add URL"):
    if url_input:
        with st.spinner(f"Fetching content from {url_input}..."):
            content = fetch_content(url_input)
            if content:
                st.session_state.content_store.add_content(url_input, content)
                st.success("Content added successfully!")

# Display added URLs
if st.session_state.content_store.urls:
    st.subheader("Analyzed URLs:")
    unique_urls = list(set(st.session_state.content_store.urls))
    for url in unique_urls:
        st.write(f"- {url}")

# Question input
question = st.text_input("Ask a question about the content:")
if st.button("Get Answer"):
    if not st.session_state.content_store.documents:
        st.warning("Please add some URLs first!")
    elif question:
        with st.spinner("Searching for relevant information..."):
            results = st.session_state.content_store.find_relevant_content(question)
            
            if results:
                st.subheader("Answer")
                for i, result in enumerate(results, 1):
                    st.markdown(f"**Relevant content {i}:**")
                    st.write(result['text'])
                    st.markdown(f"*Source: {result['url']}*")
                    st.markdown(f"*Relevance score: {result['score']:.2f}*")
                    st.markdown("---")
            else:
                st.warning("No relevant information found in the provided content.")