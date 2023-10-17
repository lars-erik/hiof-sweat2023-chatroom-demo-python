from typing import Generic, Type

from flask import g
from flask_injector import request
from injector import Binder, inject, Injector

from WebSocketNotifier import WebSocketNotifier
from chatroom.commands import SendMessageCommand, CommandHandler, SendMessageCommandHandler, TCommand
from chatroom.distribution import ChatMessageNotifier
from chatroom.persistence import ChatMessageRepository, UnitOfWork
from chatroom.queries import LastMessagesQuery, QueryHandler, LastMessagesQueryHandler
from chatroom_database import SqlaUnitOfWork
from chatroom_database.SqlaRepository import SqlaChatMessageRepository



class LoggingHandler(CommandHandler[TCommand]):
    def __init__(self, inner: CommandHandler[TCommand]):
        self.inner = inner

    def execute(self, command:TCommand):
        print(f'Handling command {command}')
        self.inner.execute(command)

def create_handler(handler_type:Type[CommandHandler[TCommand]]):
    @inject
    def inner_create_handler(handler: handler_type):
        return LoggingHandler(handler)
    return inner_create_handler

def configure_dependencies(binder: Binder) -> None:
    binder.bind(UnitOfWork, to=SqlaUnitOfWork, scope=request)
    binder.bind(ChatMessageRepository, to=SqlaChatMessageRepository, scope=request)
    binder.bind(ChatMessageNotifier, to=WebSocketNotifier)
    binder.bind(CommandHandler[SendMessageCommand], to=create_handler(SendMessageCommandHandler))
    binder.bind(QueryHandler[LastMessagesQuery], to=LastMessagesQueryHandler)

