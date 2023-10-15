from flask import Flask
from flask_injector import FlaskInjector
from flask_socketio import SocketIO

from chatroom.persistence import UnitOfWork
from chatroom_database import DatabaseInitializer
from dependencies import configure_dependencies
from routes import configure_routes

app = Flask(__name__)
socketio = SocketIO(app)
the_injector = None

def commit_and_cleanup(data):
    uow = the_injector.injector.get(UnitOfWork)
    uow.commit()
    uow.close()

if __name__ == "__main__":
    configure_routes(app)

    DatabaseInitializer.initialize('sqlite:///chatroom.db')
    DatabaseInitializer.ensure_database()

    the_injector = FlaskInjector(app=app, modules=[configure_dependencies])
    app.teardown_request(commit_and_cleanup)

    socketio.run(app, allow_unsafe_werkzeug=True)