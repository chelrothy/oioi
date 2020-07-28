from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from oioi.model import session
from oioi.model.store import Store
from oioi.model.store_review import StoreReview


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