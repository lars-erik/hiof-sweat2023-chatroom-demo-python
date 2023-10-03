import uuid
from typing import Iterable

from chatroom.model.chatmessage import ChatMessage


class ChatMessageRepository:
    def get(self, id: uuid) -> ChatMessage:
        pass

    def query(self) -> Iterable[ChatMessage]:
        pass

    def add(self, message: ChatMessage):
        pass

    def delete(self, message: ChatMessage):
        pass
