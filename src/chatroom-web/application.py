from flask import Flask
from flask_socketio import SocketIO

from dependencies import configure_dependencies
from websockets import configure_sockets
from routes import configure_routes
from flask_injector import FlaskInjector

app = Flask(__name__)
socketio = SocketIO(app)

if __name__ == "__main__":
    configure_routes(app)
    configure_sockets(socketio)

    FlaskInjector(app=app, modules=[configure_dependencies])

    socketio.run(app, allow_unsafe_werkzeug=True)