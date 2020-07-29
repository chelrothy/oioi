import os
from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from model import session
from model.store import Store
from model.store_review import StoreReview
from model.product_review import ProductReview
from model.product import Product
from controller import product_average_score_calculation


def store_detail(store_id):

    try:
        store = session.query(Store).filter(Store.id == store_id).first()

        if store:
            store_reviews = session.query(StoreReview).filter(StoreReview.store_id == store_id).all()
            products = session.query(Product).filter(Product.store_id == store_id).all()

            return {
                "id": store.id,
                "ranking": store.ranking,
                "name": store.name,
                "description": store.description,
                "average_score": store.average_score,
                "average_price": store.average_price,
                "picture": os.getenv('BASE_URL') + store.picture,
                "store_review": [{
                    "content": store_review.content,
                    "score": store_review.score,
                    "datetime": str(store_review.datetime)
                }for store_review in store_reviews],
                "products": [{
                    "product_id": product.id,
                    "name": product.name,
                    "picture": os.getenv('BASE_URL') + product.picture,
                    "average_score": product_average_score_calculation(product.id),
                    "reviews": [{
                        "content": review.content,
                        "score": review.score,
                        "datetime": str(review.datetime)
                    }for review in session.query(ProductReview).filter(ProductReview.product_id == product.id).all()]
                }for product in products]
            }

        else:
            return abort(404, "not found")

    except SQLAlchemyError:
        session.rollback()
        return abort(500, "database error")
