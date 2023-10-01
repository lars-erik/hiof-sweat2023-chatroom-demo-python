import approvaltests

from chatroom.persistence.FakeChatMessageRepository import FakeChatMessageRepository
from src.chatroom.commands.SendMessageCommand import SendMessageCommand
from src.chatroom.persistence.ChatMessageRepository import ChatMessageRepository


class Test_when_sending_messages:
    def test_messages_are_stored_in_database(self):
        repository = FakeChatMessageRepository()

        command = SendMessageCommand(repository)
        command.user = "Luke Skywalker"
        command.message = "This is Red Leader. We're approaching the Ison Corridor!"
        command.execute()

        message = repository.query()[-1]
        approvaltests.verify_as_json(message)

