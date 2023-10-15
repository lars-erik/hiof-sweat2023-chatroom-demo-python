from chatroom.persistence.Query import Query
from persistence import FakeChatMessageRepository


class FakeQuery(Query):

    def __init__(self, all):
        self.all = all

    def __iter__(self):
        return self.all.__iter__()

    def __len__(self):
        return len(self.all)

    def __getitem__(self, item):
        return self.all[item]

    def count(self):
        return len(self.all)

    def skip(self, count):
        return FakeQuery(self.all[count:])

    def limit(self, max):
        return FakeQuery(self.all[0:max])

    def order_by_descending(self, name):
        items = self.all
        items.sort(key=lambda x: x.__dict__[name], reverse=True)
        return FakeQuery(items)