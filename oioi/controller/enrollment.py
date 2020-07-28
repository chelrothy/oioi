from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from model import session
from model.store import Store
from model.product import Product


def enrollment_store(store_name, description, score, average_price, picture_url):

    try:
        add_store = Store(name=store_name, description=description, average_price=average_price,
                          picture=picture_url, average_score=score)

        session.add(add_store)
        session.commit()

        return {
            "message": "success for create store information"
        }

    except SQLAlchemyError:
        return abort(500, "database_error")


def enrollment_store_product(store_id, product_name, picture_url):

    try:
        add_product = Product(store_id=store_id, name=product_name, picture=picture_url)

        session.add(add_product)
        session.commit()

        return {
            "message": "success for create store product"
        }

    except SQLAlchemyError:
        return abort(500, "database_error")
