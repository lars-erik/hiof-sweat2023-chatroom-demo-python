from injector import inject

from chatroom.persistence import ChatMessageRepository


def configure_routes(app):

    @app.route('/')
    @inject
    def index(repo:ChatMessageRepository):
        return "<html><body><h1>Hello world " + str(len(repo.query())) + "</h1></body></html>"