from injector import Module, Binder, ClassProvider

from chatroom.persistence import ChatMessageRepository
from persistence.FakeChatMessageRepository import FakeChatMessageRepository

def configure_dependencies(binder: Binder) -> None:
    binder.bind(ChatMessageRepository, to=FakeChatMessageRepository)