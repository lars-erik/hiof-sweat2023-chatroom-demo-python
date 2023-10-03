class ChatMessage:

    def __init__(self, id, user, message) -> None:
        self.id = str(id)
        self.user = user
        self.message = message
