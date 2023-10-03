from src.chatroom.persistence.ChatMessageRepository import ChatMessageRepository


class FakeChatMessageRepository(ChatMessageRepository):

    def __init__(self) -> None:
        self.items = []

    def get(self, id):
        return [item for item in self.items if item.id == id][0]

    def query(self):
        return self.items

    def add(self, message):
        self.items.append(message)

    def delete(self, message):
        self.items.remove(message)
