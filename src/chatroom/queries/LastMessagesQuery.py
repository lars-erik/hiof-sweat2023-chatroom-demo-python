from injector import inject

from chatroom.model import ChatMessage
from chatroom.persistence import ChatMessageRepository
from chatroom.queries.abstractions import Query, QueryHandler


class LastMessagesQuery(Query):
    def __init__(self, limit = 10):
        self.limit = limit

class LastMessagesQueryHandler(QueryHandler[LastMessagesQuery]):

    @inject
    def __init__(self, repo:ChatMessageRepository):
        self.repo = repo

    def execute(self, query):
        result = (
            self.repo.query()
                .order_by_descending(ChatMessage.time)
                .limit(query.limit)
        )
        return result

