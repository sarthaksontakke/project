from dotenv import load_dotenv
load_dotenv() ## Loading all the enviroment variables

import streamlit as st
import os
import google.generativeai as genai
from  PIL import Image
# Set up API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# FUntion to Load Gemini Pro Vision Model and Gemini Pro Model
model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input ,image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

# # INITIALIZE A STREAMLITE APP

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")

input = st.text_input("Input Prompt : ",key= "input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st. image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about image")

#When submit is clicked
if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Response is ")
    st.write(response)

