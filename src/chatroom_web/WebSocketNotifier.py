import json

from flask_socketio import emit

from chatroom.distribution import ChatMessageNotifier
from chatroom.model import ChatMessage


class WebSocketNotifier(ChatMessageNotifier):
    def notify(self, message: ChatMessage):
        emit('chatmessage', {
            "time": message.time.isoformat(),
            "user": message.user,
            "message": message.message
        }, namespace='/', broadcast=True)