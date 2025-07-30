from shared.event_bus import event_bus

MOODS = ["neutral", "snarky"]
current_mood = "neutral"


def set_mood(mood: str):
    global current_mood
    if mood in MOODS:
        current_mood = mood
        event_bus.add_log(f"Mood set to {mood}")


def get_mood() -> str:
    return current_mood
