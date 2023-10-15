import uuid
from typing import Iterable

from chatroom.model.chatmessage import ChatMessage
from chatroom.persistence import Query


class ChatMessageRepository:

    def get(self, id: uuid) -> ChatMessage:
        pass

    def query(self) -> Query:
        pass

    def add(self, message: ChatMessage):
        pass

    def delete(self, message: ChatMessage):
        pass
