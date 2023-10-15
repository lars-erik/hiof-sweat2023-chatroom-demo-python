import os
from datetime import datetime

import pytest

from chatroom.commands import SendMessageCommand
from chatroom.distribution import ChatMessageNotifier
from chatroom.model import ChatMessage, TimeFactory
from chatroom.persistence import UnitOfWork
from chatroom_database import SqlaRepository, SqlaUnitOfWork, DatabaseInitializer
from persistence import FakeChatMessageRepository

TimeFactory.Now = lambda: datetime(2023, 10, 10, 10, 10, 10)

integration = os.getenv('Integration') == 'True'

if integration:
    DatabaseInitializer.initialize('sqlite:///students.db')

@pytest.fixture
def unit_of_work():
    if integration:
        DatabaseInitializer.recreate_database()
        uow = SqlaUnitOfWork()
        yield uow
        uow.close()
        DatabaseInitializer.remove_database()
    return UnitOfWork()

@pytest.fixture
def repository(unit_of_work):
    return SqlaRepository(unit_of_work, ChatMessage, 'id') if integration else FakeChatMessageRepository()

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
