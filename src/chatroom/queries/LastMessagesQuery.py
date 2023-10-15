from injector import inject

from chatroom.model import ChatMessage
from chatroom.persistence import ChatMessageRepository


class LastMessagesQuery():

    @inject
    def __init__(self, repo:ChatMessageRepository):
        self.repo = repo

    def execute(self):
        result = (
            self.repo.query()
                .order_by_descending(ChatMessage.time)
                .limit(10)
        )
        return result

