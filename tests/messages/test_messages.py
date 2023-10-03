import approvaltests
import pytest
from approvaltests import Options
from approvaltests.scrubbers import scrub_all_guids

from persistence.FakeChatMessageRepository import FakeChatMessageRepository
from chatroom.commands.SendMessageCommand import SendMessageCommand


class Test_when_sending_messages:

    @pytest.fixture
    def repository(self):
        return FakeChatMessageRepository()

    def test_messages_are_stored_in_database(self, repository):
        command = SendMessageCommand(repository)
        command.user = "Luke Skywalker"
        command.message = "This is Red Leader. We're approaching the Ison Corridor!"
        command.execute()

        message = repository.query()[-1]
        approvaltests.verify_as_json(message, options=Options().with_scrubber(scrub_all_guids))

