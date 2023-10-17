import uuid
from datetime import datetime

import approvaltests

from chatroom.model import ChatMessage, TimeFactory
from chatroom.queries import LastMessagesQuery, LastMessagesQueryHandler


class Test_when_joining_chatroom:

    def test_last_ten_messages_are_shown(self, repository):
        for i in range(0, 11):
            TimeFactory.Now = lambda: datetime(2023, 10, 10, 10, 10, i)
            repository.add(ChatMessage(uuid.uuid4(), "Me", str(i)))

        query = LastMessagesQuery()
        result = LastMessagesQueryHandler(repository).execute(query)

        approvaltests.verify_all("Chat log", result)