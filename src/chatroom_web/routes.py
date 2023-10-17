from flask import render_template, request, Response
from injector import inject

from chatroom.commands import SendMessageCommand, CommandHandler
from chatroom.queries import LastMessagesQuery, QueryHandler


def configure_routes(app):

    @app.route('/')
    @inject
    def index(handler:QueryHandler[LastMessagesQuery]):
        return render_template(
            "index.html",
            messages=handler.execute(LastMessagesQuery())
        )

    @app.route('/chat', methods=['POST'])
    @inject
    def chat(handler:CommandHandler[SendMessageCommand]):
        cmd = SendMessageCommand()
        cmd.__dict__.update(request.json)
        handler.execute(cmd)
        return Response(status=200)