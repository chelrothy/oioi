from flask_restful import Resource

from controller.store import store_detail


class Store(Resource):

    def get(self, store_id):

        return store_detail(store_id)
