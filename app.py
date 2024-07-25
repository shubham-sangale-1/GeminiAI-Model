import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
key = os.getenv("GOOGLE_API_KEY")

if not key:
    raise ValueError("API key not found in environment variables")

genai.configure(api_key=key)

st.title("Welcome to my Streamlit app")

name = st.text_input("Ask me anything!")

if st.button("Generate"):
    if name:
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(name)
            st.text_area("Response", response.text, height=500)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt.")
st.markdown("<h5 style='color: green;'>Developer : Shubham Sangale</h5><br><a href='https://www.linkedin.com/in/shubham-sangale-81568722a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app'><h6 style='color: blue;'>Linkedin</h6></a>", unsafe_allow_html=True)
