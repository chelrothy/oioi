import os
from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from router import bp_basic


def create_app():

    _app = Flask(__name__)

    CORS(_app, resources={
        r"/api/*": {"origin": "*"}
    })

    _app.register_blueprint(bp_basic)

    _app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
    _app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

    JWTManager(app=_app)

    return _app
