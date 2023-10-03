import uuid

from injector import inject

from chatroom.distribution.ChatMessageNotifier import ChatMessageNotifier
from chatroom.model.chatmessage import ChatMessage
from chatroom.persistence import ChatMessageRepository


class SendMessageCommand:

    @inject
    def __init__(self, repository: ChatMessageRepository, notifier: ChatMessageNotifier) -> None:
        self.repository = repository
        self.notifier = notifier
        self.user = ""
        self.message = ""

    def execute(self):
        message = ChatMessage(uuid.uuid4(), self.user, self.message)
        self.repository.add(message)
        self.notifier.notify(message)