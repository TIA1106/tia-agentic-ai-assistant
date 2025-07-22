import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1"
)

def ask_agentic_ai(messages):
    response = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        messages=messages,
        temperature=0.7,
    )
    return response.choices[0].message.content
