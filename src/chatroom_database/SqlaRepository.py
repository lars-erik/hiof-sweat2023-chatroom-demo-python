from injector import inject

from chatroom.model import ChatMessage
from chatroom.persistence import ChatMessageRepository
from chatroom_database import SqlaUnitOfWork
from chatroom_database.QueryWrapper import QueryWrapper

class SqlaRepository(ChatMessageRepository):

    def __init__(self, uow, entity_class, primary_key):
        self.uow = uow
        self.entity_class = entity_class
        self.primary_key = primary_key

    def add(self, entity):
        self.uow.session.add(entity)

    def update(self, entity):
        self.uow.session.merge(entity)

    def delete(self, entity):
        self.uow.session.delete(entity)

    def get(self, id):
        return self.uow.session.query(self.entity_class).filter(getattr(self.entity_class, self.primary_key) == id).first()

    def query(self):
        return QueryWrapper(self.uow.session.query(self.entity_class))

class SqlaChatMessageRepository(SqlaRepository):

    @inject
    def __init__(self, uow: SqlaUnitOfWork):
        super().__init__(uow, ChatMessage, "id")