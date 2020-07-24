from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from oioi.model import session
from oioi.model.store import Store
from oioi.model.store_review import StoreReview
from oioi.model.product_review import ProductReview


def create_store_review(store_id, content, score, reviewer):

    try:
        store = session.query(Store).filter(Store.id == store_id).first()

        if store:
            add_review = StoreReview(store_id=store_id, content=content, score=score, reviewer=reviewer)

            session.add(add_review)
            session.commit()

            return {
                "message": "success for create store review"
            }, 201

        else:
            abort(400, "bad request")

    except SQLAlchemyError:
        return abort(500, "database error")


def create_product_review(store_id, name, content, score, picture, reviewer):

    try:
        store = session.query(Store).filter(Store.id == store_id).first()

        if store:
            picture_location = '/static/' + str(picture.filename)
            picture.save(picture_location)

            add_review = ProductReview(store_id=store_id, name=name, content=content, picture=picture_location,
                                       score=score, reviewer=reviewer)

            session.add(add_review)
            session.commit()

            return {
                "message": "success for created product reveiw"
            }, 201

        else:
            return abort(404, "not found store")

    except SQLAlchemyError:
        return abort(500, "database error")
