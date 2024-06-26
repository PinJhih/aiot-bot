import os

import google.generativeai as genai
from dotenv import load_dotenv

import raspberry
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
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction="""
        你現在被部署在一台 raspberry pi 3 上，並且作為一個 Discord 伺服器的聊天機器人。
        你現在可以透過我提供給你的 function，查詢最近台灣各縣市的天氣、讀取目前的氣溫和濕度，以及控制 raspberry 連結的電燈的能力。
        請你依照大家的訊息，並利用我提供的 function，盡可能取得所需的資訊，並給出適當的建議和操作。
        """,
    tools=[
        weather.get_weather_data,
        raspberry.turn_on_classroom_light,
        raspberry.turn_on_lab_light,
        raspberry.turn_off_classroom_light,
        raspberry.turn_off_lab_light,
    ],
)

chat = model.start_chat(enable_automatic_function_calling=True)


def send_message(message):
    response = chat.send_message(message)
    return response.text


def send_image(message, image):
    response = chat.send_message([message, image])
    return response.text
