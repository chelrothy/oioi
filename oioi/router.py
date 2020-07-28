from flask import Blueprint
from flask_restful import Api

bp_basic = Blueprint("auth", __name__, url_prefix="/api/v1")
api_basic = Api(bp_basic)

from view.auth import SignUp
api_basic.add_resource(SignUp, "/signup")

from view.auth import Login
api_basic.add_resource(Login, "/login")

from view.ranking import Ranking
api_basic.add_resource(Ranking, "/store/ranking")

from view.store import Store
api_basic.add_resource(Store, "/<store_id>")

from view.review import StoreReview
api_basic.add_resource(StoreReview, "/<store_id>/review")

from view.review import ProductReview
api_basic.add_resource(ProductReview, "/<store_id>/review/<product_id>")

from view.enrollment import EnrollmentStore
api_basic.add_resource(EnrollmentStore, "/store")

from view.enrollment import EnrollmentStoreProduct
api_basic.add_resource(EnrollmentStoreProduct, "/<store_id>/product")
