# Penny V9

Penny is a sarcastic AI-powered Twitch streamer. This repository contains a FastAPI backend and a React frontend. Penny listens to Twitch chat, responds using OpenAI, and speaks through a local Piper TTS engine.

## Running

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

2. Install frontend dependencies:

```bash
cd frontend && npm install
```

3. Set environment variables in a `.env` file:

```
OPENAI_API_KEY=your_key
TWITCH_OAUTH_TOKEN=oauth:token
TWITCH_CHANNEL=yourchannel
TWITCH_CLIENT_ID=client_id
TWITCH_CLIENT_SECRET=client_secret
TWITCH_CHANNEL_ID=channel_id
```

4. Start the backend:

```bash
uvicorn backend.main:app --reload
```

5. Start the frontend:

```bash
npm run dev
```

The frontend shows chat messages, Twitch events, and console logs. Use the input box to talk to Penny.
