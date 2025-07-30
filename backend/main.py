from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.services import (
    personality_engine,
    tts_service,
    mood_service,
    twitch_chat,
    twitch_eventsub,
)
from shared.event_bus import event_bus
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


@app.on_event("startup")
async def startup_event():
    twitch_chat.start_bot()
    twitch_eventsub.start_eventsub()
    event_bus.add_log("Backend started")


@app.post("/api/speak")
def speak(req: SpeakRequest, background_tasks: BackgroundTasks):
    prompt = personality_engine.inject_personality(req.text, mood_service.get_mood())
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Penny, a snarky but sweet AI streamer assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.9,
            max_tokens=200,
        )
        reply = response.choices[0].message.content
        background_tasks.add_task(tts_service.speak, reply)
        event_bus.add_log(f"Penny: {reply}")
        return {"response": reply}
    except Exception as e:
        event_bus.add_log(f"OpenAI error: {e}")
        return {"error": str(e)}


@app.get("/api/chat")
def get_chat():
    return {"messages": event_bus.get_chats()}


@app.get("/api/events")
def get_events():
    return {"events": event_bus.get_events()}


@app.get("/api/logs")
def get_logs():
    return {"logs": event_bus.get_logs()}
