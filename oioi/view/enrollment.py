from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from werkzeug import secure_filename

from oioi.view import check_json
from oioi.controller.enrollment import enrollment_store, enrollment_store_product


class EnrollmentStore(Resource):

    @jwt_required
    @check_json({
        "store_name": str,
        "description": str,
        "score": int,
        "average_price": int
    })
    def post(self):
        store_name = request.json['store_name']
        description = request.json['description']
        score = request.json['score']
        average_price = request.json['average_price']
        picture = request.files['picture']
        picture.save("/static/store_image", secure_filename(picture.filename))

        picture_url = f"/static/store_image/{picture.filename}"

        return enrollment_store(store_name, description, score, average_price, picture_url)


class EnrollmentStoreProduct(Resource):

    @jwt_required
    @check_json({
        "product_name": str
    })
    def post(self, store_id):
        product_name = request.json['product_name']
        picture = request.files['picture']
        picture.save("/static/product_image", secure_filename(picture.filename))

        picture_url = f"/static/product_image/{picture.filename}"

        return enrollment_store_product(store_id, product_name, picture_url)
