from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.services import personality_engine
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SpeakRequest(BaseModel):
    text: str

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/api/speak")
def speak(req: SpeakRequest):
    prompt = personality_engine.inject_personality(req.text)

    try:
        response = client.chat.completions.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are Penny, a snarky but sweet AI streamer assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            max_tokens=200,
        )
        reply = response.choices[0].message.content
        return {"response": reply}

    except Exception as e:
        return {"error": str(e)}