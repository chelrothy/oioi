from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from oioi import (JWT_SECRET_KEY, JWT_REFRESH_TOKEN_EXPIRES,
                  JWT_ACCESS_TOKEN_EXPIRES)

from oioi.router import bp_basic


def create_app():

    _app = Flask(__name__)

    CORS(_app, resources={
        r"/api/*": {"origin": "*"}
    })

    _app.register_blueprint(bp_basic)

    _app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    _app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
    _app.config['JWT_REFRESH_TOKEN_EXPIRES'] = JWT_REFRESH_TOKEN_EXPIRES

    JWTManager(app=_app)

    return _app
