import approvaltests
import pytest
from approvaltests import Options
from approvaltests.scrubbers import scrub_all_guids

from chatroom.commands import SendMessageCommand
from chatroom.distribution import ChatMessageNotifier
from chatroom.model import ChatMessage
from persistence import FakeChatMessageRepository

approval_options = Options().with_scrubber(scrub_all_guids)

class SpyChatMessageNotifier(ChatMessageNotifier):
    def __init__(self) -> None:
        self.messages = []

    def notify(self, message: ChatMessage):
        self.messages.append(message)

    def last(self):
        return self.messages[-1]


class Test_when_sending_messages:

    @pytest.fixture
    def repository(self):
        return FakeChatMessageRepository()

    @pytest.fixture
    def notifier(self):
        return SpyChatMessageNotifier()

    @pytest.fixture
    def command(self, repository, notifier):
        return SendMessageCommand(repository, notifier)

    def test_messages_are_stored_in_database(self, command, repository):
        command.user = "Luke Skywalker"
        command.message = "This is Red Leader. We're approaching the Ison Corridor!"
        command.execute()

        message = repository.query()[-1]
        approvaltests.verify_as_json(message, options=approval_options)

    def test_messages_are_broadcast_to_everyone(self, command, notifier):
        command.user = "Luke Skywalker"
        command.message = "This is Red Leader. We're approaching the Ison Corridor!"
        command.execute()

        approvaltests.verify_as_json(notifier.last(), options=approval_options)
