import streamlit as st
import PyPDF2
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import re
from collections import Counter

# Download NLTK stop words
nltk.download('stopwords')

# Define a function to preprocess text
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove special characters, numbers, and punctuation
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenize text
    words = text.split()
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return words

# Streamlit app
st.title("PDF Word Cloud Generator")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    try:
        # Extract text from PDF
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Preprocess text
        words = preprocess_text(text)

        # Generate word frequencies
        word_freq = Counter(words)

        # Create a word cloud
        wordcloud = WordCloud(width=800, height=400, max_words=500, background_color='white').generate_from_frequencies(word_freq)

        # Display the word cloud
        st.subheader("Word Cloud")
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)
    except Exception as e:
        st.error(f"An error occurred: {e}")
