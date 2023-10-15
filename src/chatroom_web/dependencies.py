from flask import g
from flask_injector import request
from injector import Binder

from WebSocketNotifier import WebSocketNotifier
from chatroom.commands import SendMessageCommand
from chatroom.distribution import ChatMessageNotifier
from chatroom.persistence import ChatMessageRepository, UnitOfWork
from chatroom.queries import LastMessagesQuery
from chatroom_database import SqlaUnitOfWork
from chatroom_database.SqlaRepository import SqlaChatMessageRepository

def configure_dependencies(binder: Binder) -> None:
    binder.bind(UnitOfWork, to=SqlaUnitOfWork, scope=request)
    binder.bind(ChatMessageRepository, to=SqlaChatMessageRepository, scope=request)
    binder.bind(ChatMessageNotifier, to=WebSocketNotifier)
    binder.bind(SendMessageCommand, to=SendMessageCommand)
    binder.bind(LastMessagesQuery, to=LastMessagesQuery)

