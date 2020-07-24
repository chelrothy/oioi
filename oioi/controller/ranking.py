from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from oioi.model import session
from oioi.model.store import Store


def ranking(search):

    try:
        stores = session.query(Store).filter(Store.name.like(f'%{search}%')).order_by(Store.ranking).all()

        if stores:
            return [{
                "id": store.id,
                "ranking": store.ranking,
                "name": store.name,
                "description": store.description,
                "score": store.score,
                "average_price": store.average_score,
                "picture": store.picture
            }for store in stores]

        else:
            abort(400, "none data")

    except SQLAlchemyError:
        abort(500, "database error")
