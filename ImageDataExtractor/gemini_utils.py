import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image

class GeminiUtils:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=self.api_key)

    def get_gemini_response(self, input, image, prompt):
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([input, image[0], prompt])
        return response.text

    def input_image_setup(self, uploaded_file):
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            image_parts = [
                {
                    "mime_type": uploaded_file.type,
                    "data": bytes_data
                }
            ]
            return image_parts
        else:
            raise FileNotFoundError("No file uploaded")
