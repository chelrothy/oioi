from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from oioi.model import session
from oioi.model.store import Store
from oioi.model.store_review import StoreReview
from oioi.model.product_review import ProductReview
from oioi.model.product import Product


def store_detail(store_id):

    try:
        store = session.query(Store).filter(Store.id == store_id).first()

        if store:
            store_reviews = session.query(StoreReview).filter(StoreReview.store_id == store_id).all()
            products = session.query(Product).filter(Product.store_id == store_id).all()
            product_reviews = session.query(ProductReview).filter(ProductReview.product_id == product.id).all()

            return {
                "id": store.id,
                "ranking": store.ranking,
                "name": store.name,
                "description": store.description,
                "score": store.score,
                "average_price": store.average_score,
                "picture": store.picture,
                "store_review": [{
                    "content": store_review.content,
                    "score": store_review.score,
                    "datetime": str(store_review.datetime),
                    "reviewer": store_review.reviewer
                }for store_review in store_reviews],
                "products": [{
                    "name": product.name,
                    "picture": product.picture,
                    "reviews": [{
                        "content": review.content,
                        "score": review.score,
                        "datetime": str(review.datetime),
                        "reviewer": review.reviewer,
                    }for review in session.query(ProductReview).filter(ProductReview.product_id == product.id).all()]
                }for product in products]
            }

        else:
            return abort(404, "not found ")

    except SQLAlchemyError:
        return abort(500, "database error")
