from collections import deque
from threading import Lock

class EventBus:
    def __init__(self, maxlen: int = 100):
        self.chat_messages = deque(maxlen=maxlen)
        self.events = deque(maxlen=maxlen)
        self.logs = deque(maxlen=maxlen)
        self._lock = Lock()

    def add_chat(self, message: str) -> None:
        with self._lock:
            self.chat_messages.append(message)

    def add_event(self, event: str) -> None:
        with self._lock:
            self.events.append(event)

    def add_log(self, log: str) -> None:
        with self._lock:
            self.logs.append(log)

    def get_chats(self):
        with self._lock:
            return list(self.chat_messages)

    def get_events(self):
        with self._lock:
            return list(self.events)

    def get_logs(self):
        with self._lock:
            return list(self.logs)

event_bus = EventBus()
