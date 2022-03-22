from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    from .views.api import api
    from .views.error_handler import error_handler
    app.register_blueprint(api)
    app.register_blueprint(error_handler)

    return app
