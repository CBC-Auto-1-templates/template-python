from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.get("/hello")
    def get_hello():
        return "Hello World!"

    return app


def main():
    create_app()


