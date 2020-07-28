import datetime
from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from model import session
from model.store import Store
from model.store_review import StoreReview
from model.product_review import ProductReview
from controller import average_score_calculation


def create_store_review(store_id, content, score, reviewer):

    try:
        store = session.query(Store).filter(Store.id == store_id).first()

        if store:
            add_review = StoreReview(store_id=store_id, content=content, score=score, reviewer=reviewer,
                                     datetime=datetime.datetime.now())

            session.add(add_review)
            session.commit()

            average_score_calculation(store_id)

            return {
                "message": "success for create store review"
            }, 201

        else:
            abort(400, "bad request")

    except SQLAlchemyError:
        session.rollback()
        return abort(500, "database error")


def create_product_review(product_id, content, score, reviewer):

    try:

        add_review = ProductReview(product_id=product_id, content=content,
                                   score=score, reviewer=reviewer, datetime=datetime.datetime.now())

        session.add(add_review)
        session.commit()

        return {
            "message": "success for created product review"
        }, 201

    except SQLAlchemyError:
        session.rollback()
        return abort(500, "database error")
