import uuid
from typing import Iterable

from chatroom.model.chatmessage import ChatMessage
from chatroom.persistence.ChatMessageRepository import ChatMessageRepository


class FakeChatMessageRepository(ChatMessageRepository):

    def __init__(self) -> None:
        self.items = []

    def get(self, id: uuid) -> ChatMessage:
        return [item for item in self.items if item.id == id][0]

    def query(self) -> Iterable[ChatMessage]:
        return self.items

    def add(self, message: ChatMessage):
        self.items.append(message)

    def delete(self, message: ChatMessage):
        self.items.remove(message)
