import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# Load vectorizer and classifier
vectorizer = joblib.load("vectorizer.pkl")
classifier = joblib.load("classifier.pkl")

# Function to predict if the news is real or fake
def predict_news(text):
    vectorized_text = vectorizer.transform([text])
    prediction = classifier.predict(vectorized_text)
    return prediction[0]

# Streamlit app setup
st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

st.title("📰 Fake News Detection App")
st.info("Enter the news article text below to check if it's real or fake.")

text_input = st.text_area("News Article Text", height=200, placeholder="Type or paste the news article text here...")

if st.button("Check"):
    prediction = predict_news(text_input)
    st.write("---")

    if prediction == 0:
        st.success("✅ This news article is **REAL**.")
    else:
        st.error("🚫 This news article is **FAKE**.")
