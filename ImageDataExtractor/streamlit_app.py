import streamlit as st
from gemini_utils import GeminiUtils

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")

gemini_utils = GeminiUtils()

input_prompt = """
               You have provided stock market data 
               please provide the details of items
               in below format

               1. Item 1 - Market Cap
               2. Item 2 - Current Price
               ----
               ----
               """

input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = ""   
if uploaded_file is not None:
    image = st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

if submit:
    image_data = gemini_utils.input_image_setup(uploaded_file)
    response = gemini_utils.get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is")
    st.write(response)
