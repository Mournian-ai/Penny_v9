import os
from twitchAPI.twitch import Twitch
from shared.event_bus import event_bus

CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")
CHANNEL_ID = os.getenv("TWITCH_CHANNEL_ID")


def start_eventsub():
    try:
        if not CLIENT_ID or not CLIENT_SECRET or not CHANNEL_ID:
            event_bus.add_log("EventSub credentials not configured")
            return
        twitch = Twitch(CLIENT_ID, CLIENT_SECRET)
        twitch.authenticate_app([])
        event_bus.add_event("EventSub connected")
    except Exception as e:
        event_bus.add_log(f"EventSub error: {e}")
