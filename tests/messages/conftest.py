from datetime import datetime

import pytest

from chatroom.commands import SendMessageCommand
from chatroom.distribution import ChatMessageNotifier
from chatroom.model import ChatMessage, TimeFactory
from persistence import FakeChatMessageRepository

TimeFactory.Now = lambda: datetime(2023, 10, 10, 10, 10, 10)

@pytest.fixture
def repository():
    return FakeChatMessageRepository()

@pytest.fixture
def notifier():
    return SpyChatMessageNotifier()

@pytest.fixture
def command(repository, notifier):
    return SendMessageCommand(repository, notifier)


class SpyChatMessageNotifier(ChatMessageNotifier):
    def __init__(self) -> None:
        self.messages = []

    def notify(self, message: ChatMessage):
        self.messages.append(message)

    def last(self):
        return self.messages[-1]
