from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from controller.enrollment import enrollment_store, enrollment_store_product


class EnrollmentStore(Resource):

    @jwt_required
    def post(self):
        store_name = request.form['store_name']
        description = request.form['description']
        score = request.form['score']
        average_price = request.form['average_price']
        picture = request.files['picture']
        picture.save("static/store_image/" + picture.filename)

        picture_url = "static/store_image/" + picture.filename

        return enrollment_store(store_name, description, score, average_price, picture_url)


class EnrollmentStoreProduct(Resource):

    @jwt_required
    def post(self, store_id):
        product_name = request.form['product_name']
        picture = request.files['picture']
        picture.save("static/product_image/" + picture.filename)

        picture_url = "static/product_image/" + picture.filename

        return enrollment_store_product(store_id, product_name, picture_url)
