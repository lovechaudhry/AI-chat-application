import streamlit as st
from modules.chatbot import handle_query

st.title("AI Chat with PDF Knowledge Base")

uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
user_input = st.text_input("Ask a question:")

if st.button("Submit") and user_input:
    if uploaded_files:
        response = handle_query(user_input, uploaded_files)
        st.write(response)
    else:
        st.write("Please upload PDFs to query.")
