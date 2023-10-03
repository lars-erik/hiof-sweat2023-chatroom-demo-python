from flask import Flask
from configure_dependencies import configure_dependencies
from routes import configure_routes
from flask_injector import FlaskInjector

app = Flask(__name__)

if __name__ == "__main__":
    configure_routes(app)

    FlaskInjector(app=app, modules=[configure_dependencies])

    app.run()