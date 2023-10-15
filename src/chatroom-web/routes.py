from flask import render_template, jsonify, request, Response
from injector import inject

from chatroom.commands import SendMessageCommand
from chatroom.queries import LastMessagesQuery


def configure_routes(app):

    @app.route('/')
    @inject
    def index(query:LastMessagesQuery):
        return render_template(
            "index.html",
            messages=query.execute()
        )

    @app.route('/chat', methods=['POST'])
    @inject
    def chat(cmd:SendMessageCommand):
        cmd.__dict__.update(request.json)
        cmd.execute()
        return Response(status=200)