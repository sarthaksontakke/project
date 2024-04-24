from dotenv import load_dotenv
load_dotenv() ## Loading all the enviroment variables

import streamlit as st
import os
import google.generativeai as genai

# Set up API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# FUntion to Load Gemini MOdel and Gemini Pro Model
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# # INITIALIZE A STREAMLITE APP

st.set_page_config(page_title="Q&A DEMO APPLICATION")

st.header("GeminiLLM Application")

input = st.text_input("Input : ",key= "input")

submit  = st.button("Ask a Question")

#When submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is ")
    st.write(response)