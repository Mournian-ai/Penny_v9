from collections import deque
from threading import Lock

class ResponseQueue:
    def __init__(self, maxlen: int = 100):
        self._queue = deque(maxlen=maxlen)
        self._lock = Lock()

    def push(self, item: str) -> None:
        with self._lock:
            self._queue.append(item)

    def pop(self):
        with self._lock:
            if self._queue:
                return self._queue.popleft()

    def items(self):
        with self._lock:
            return list(self._queue)

response_queue = ResponseQueue()
