import approvaltests

from chatroom.commands import SendMessageCommand


class Test_when_sending_messages:

    def test_messages_are_stored_in_database(self, send_message_handler, repository):
        command = SendMessageCommand("Luke Skywalker", "This is Red Leader. We're approaching the Ison Corridor!")
        send_message_handler.execute(command)

        message = repository.query()[0]
        approvaltests.verify(message)

    def test_messages_are_broadcast_to_everyone(self, send_message_handler, notifier):
        command = SendMessageCommand("Luke Skywalker", "This is Red Leader. We're approaching the Ison Corridor!")
        send_message_handler.execute(command)

        approvaltests.verify(notifier.last())
