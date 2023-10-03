import socketio
from injector import inject

from chatroom.persistence.ChatMessageRepository import ChatMessageRepository


def configure_sockets(socketio):

    @socketio.on('chat')
    def receive_chatmessage(data):
        # TODO: Figure out how to inject here
        print(f"Message from {data['user']}: {data['message']}")