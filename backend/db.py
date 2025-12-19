import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Sentiment Dashboard", layout="centered")

st.title("🧠 Product Sentiment Analysis Dashboard")

text = st.text_area("Enter Product Review")

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Analyze"):
    response = requests.post(
        "http://127.0.0.1:5000/analyze",
        json={"text": text}
    )
    sentiment = response.json()["sentiment"]

    st.success(f"Sentiment: {sentiment}")
    st.session_state.history.append(sentiment)

# Dashboard analytics
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history, columns=["Sentiment"])
    st.subheader("📊 Sentiment Distribution")
    st.bar_chart(df["Sentiment"].value_counts())