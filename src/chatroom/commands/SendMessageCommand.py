import uuid

from injector import inject

from chatroom.commands.abstractions import Command, CommandHandler
from chatroom.distribution.ChatMessageNotifier import ChatMessageNotifier
from chatroom.model.chatmessage import ChatMessage
from chatroom.persistence import ChatMessageRepository


class SendMessageCommand(Command):

    @inject
    def __init__(self, user = "", message = "") -> None:
        self.user = user
        self.message = message

class SendMessageCommandHandler(CommandHandler[SendMessageCommand]):

    @inject
    def __init__(self, repository: ChatMessageRepository, notifier: ChatMessageNotifier) -> None:
        self.repository = repository
        self.notifier = notifier

    def execute(self, command:SendMessageCommand):
        message = ChatMessage(uuid.uuid4(), command.user, command.message)
        self.repository.add(message)
        self.notifier.notify(message)