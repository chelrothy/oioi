from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from model import session
from model.store import Store
from model.store_review import StoreReview
from model.product_review import ProductReview


def average_score_calculation(store_id):

    try:
        store = session.query(Store).filter(Store.id == store_id).first()

        store_reviews = session.query(StoreReview).filter(StoreReview.store_id == store_id).all()

        average_score = 0
        for review in store_reviews:
            average_score += review.score

        average_score = average_score // len(store_reviews)

        store.average_score = average_score
        session.commit()

    except SQLAlchemyError:
        return abort(500, "database error")


def product_average_score_calculation(product_id):

    try:
        product_reviews = session.query(ProductReview).filter(ProductReview.product_id == product_id).all()

        if product_reviews:
            average_score = 0
            for review in product_reviews:
                average_score += review.score

            average_score = average_score // len(product_reviews)

            return average_score
        else:
            return 0

    except SQLAlchemyError:
        return abort(500, "database error")