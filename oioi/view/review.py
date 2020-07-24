from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from oioi.controller.review import create_store_review, create_product_review
from oioi.view import check_json


class StoreReview(Resource):

    @jwt_required
    @check_json({
        "content": str,
        "score": str
    })
    def post(self, store_id):
        content = request.json['content']
        score = request.json['score']
        reviewer = get_jwt_identity()

        return create_store_review(store_id, content, score, reviewer)


class ProductReview(Resource):

    @jwt_required
    def post(self, store_id):
        name = request.json['name']
        content = request.json['content']
        score = request.json['score']
        reviewer = get_jwt_identity()

        return create_product_review(store_id, name, content, score, reviewer)
