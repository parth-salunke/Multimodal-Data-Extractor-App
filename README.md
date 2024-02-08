# Multimodel-Data-Extractor-App

---

# Gemini Image Demo

This is a Streamlit application that utilizes the Gemini API for generating content based on input text and uploaded images.

## Getting Started

To run this application locally, you'll need to follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/parth-salunke/Multimodel-Data-Extractor-App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ImageDataExtractor
   ```

3. Install the required dependencies. It's recommended to do this in a virtual environment:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables by creating a `.env` file in the project directory and adding your Google API key:

   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

5. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

6. Access the application in your web browser by navigating to `http://localhost:8501`.

## Usage

1. Provide an input prompt in the text input field.
2. Choose an image file by clicking on the "Choose an image..." button.
3. Click on the "Tell me about the image" button to generate content based on the input prompt and the uploaded image.
4. The generated response will be displayed below.

## Dependencies

- `google.generativeai`: Library for accessing the Gemini API.
- `dotenv`: Library for loading environment variables from a `.env` file.
- `PIL`: Python Imaging Library for image processing.
- `streamlit`: Library for creating interactive web applications.

## About

This application is created as a demonstration of utilizing the Gemini API in combination with Streamlit for generating content based on input text and images.



---
