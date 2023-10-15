from datetime import datetime

from chatroom.model.TimeFactory import TimeFactory


class ChatMessage:

    def __init__(self, id, user, message, time = None) -> None:
        self.id = id
        self.user = user
        self.message = message
        self.time = time or TimeFactory.Now()

    def __str__(self):
        return f"ChatMessage({str(self.time)}, {self.user}: {self.message})"