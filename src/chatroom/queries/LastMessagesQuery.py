from injector import inject

from chatroom.model import ChatMessage
from chatroom.persistence import ChatMessageRepository


class LastMessagesQuery():

    @inject
    def __init__(self, repo:ChatMessageRepository):
        self.repo = repo

    def execute(self):
        count = len(self.repo.query())
        result = self.repo.query()[count - 10:]
        result.sort(key=lambda x: x.time, reverse=True)
        return result