import uuid

from injector import inject

from chatroom.model.chatmessage import ChatMessage
from chatroom.persistence.ChatMessageRepository import ChatMessageRepository


class SendMessageCommand:

    @inject
    def __init__(self, repository: ChatMessageRepository) -> None:
        self.repository = repository
        self.user = ""
        self.message = ""

    def execute(self):
        self.repository.add(ChatMessage(uuid.uuid4(), self.user, self.message))
