from flask import request
from flask_restful import Resource

from controller.ranking import ranking


class Ranking(Resource):

    def get(self):

        search = request.args['search']

        return ranking(search)
