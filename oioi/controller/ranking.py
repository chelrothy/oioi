import os
from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from oioi.model import session
from oioi.model.store import Store


def ranking(search):

    try:
        stores = session.query(Store).filter(Store.name.like(f'%{search}%')).order_by(Store.average_score).all()

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
                "picture": f"{os.getenv('BASE_URL')}{store.picture}"
            }for index, store in enumerate(stores)]

            return response

        else:
            abort(400, "none data")

    except SQLAlchemyError:
        abort(500, "database error")
