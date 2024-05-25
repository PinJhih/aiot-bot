import os

import google.generativeai as genai
from dotenv import load_dotenv

import weather

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "temperature": 0.8,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]


model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings,
    tools=[weather.get_weather_data],
)

chat = model.start_chat(enable_automatic_function_calling=True)


def send_message(message):
    response = chat.send_message(message)
    return response.text
