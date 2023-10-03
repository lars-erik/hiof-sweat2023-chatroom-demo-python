from injector import Module, Binder, ClassProvider, singleton

from chatroom.commands.SendMessageCommand import SendMessageCommand
from chatroom.persistence import ChatMessageRepository
from persistence.FakeChatMessageRepository import FakeChatMessageRepository

def configure_dependencies(binder: Binder) -> None:
    binder.bind(ChatMessageRepository, to=FakeChatMessageRepository, scope=singleton)
    binder.bind(SendMessageCommand, to=SendMessageCommand)
