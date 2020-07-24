from flask_restful import Resource
from flask_jwt_extended import jwt_required

from oioi.controller.store import store_detail


class Store(Resource):

    @jwt_required
    def get(self, store_id):

        return store_detail(store_id)
