# app.py

import streamlit as st
import requests

st.set_page_config(page_title="Medical FAQ Assistant", page_icon="💬", layout="centered")

st.title(" Medical FAQ RAG Assistant")
st.write("hello how may i hello you ?Ask me anything about clinic timings, insurance, appointments, and more!")

# API endpoint
API_URL = "http://127.0.0.1:8000/ask"

# Input box
user_query = st.text_input("Enter your question:")

if st.button("Ask"):
    if user_query.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(API_URL, json={"query": user_query})
                if response.status_code == 200:
                    data = response.json()
                    st.success(data["answer"])
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to API: {e}")
