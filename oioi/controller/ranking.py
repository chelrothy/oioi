import os
from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from model import session
from model.store import Store


def ranking(search):

    try:
        stores = session.query(Store).filter(Store.name.like('%' + search + '%')
                                             ).order_by(Store.average_score.desc()).all()

        for index, store in enumerate(stores):
            store_info = session.query(Store).filter(Store.id == store.id).first()
            store_info.ranking = index + 1
            session.commit()

        if stores:
            response = [{
                "id": store.id,
                "ranking": store.ranking,
                "name": store.name,
                "description": store.description,
                "average_score": store.average_score,
                "average_price": store.average_price,
                "picture": os.getenv('BASE_URL') + store.picture
            }for index, store in enumerate(stores)]

            return response

        else:
            abort(400, "none data")

    except SQLAlchemyError:
        session.rollback()
        abort(500, "database error")
