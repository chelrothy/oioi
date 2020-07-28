from flask import request
from flask_restful import Resource

from oioi.view import check_json
from oioi.controller.auth import sign_up, login


class SignUp(Resource):
    @check_json({
        "id": str,
        "password": str,
        "name": str
    })
    def post(self):
        id = request.json['id']
        password = request.json['password']
        name = request.json['name']

        return sign_up(id, password, name)


class Login(Resource):

    @check_json({
        "id": str,
        "password": str
    })
    def post(self):
        id = request.json['id']
        password = request.json['password']

        return login(id, password)
