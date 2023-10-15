from injector import Binder, singleton

from WebSocketNotifier import WebSocketNotifier
from chatroom.commands import SendMessageCommand
from chatroom.distribution import ChatMessageNotifier
from chatroom.persistence import ChatMessageRepository
from chatroom.queries import LastMessagesQuery
from persistence import FakeChatMessageRepository


def configure_dependencies(binder: Binder) -> None:
    binder.bind(ChatMessageRepository, to=FakeChatMessageRepository, scope=singleton)
    binder.bind(ChatMessageNotifier, to=WebSocketNotifier)
    binder.bind(SendMessageCommand, to=SendMessageCommand)
    binder.bind(LastMessagesQuery, to=LastMessagesQuery)

