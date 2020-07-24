from flask import Blueprint
from flask_restful import Api

bp_basic = Blueprint("auth", __name__, url_prefix="/api/v1")
api_basic = Api(bp_basic)

from oioi.view.auth import SignUp
api_basic.add_resource(SignUp, "/signup")

from oioi.view.auth import Login
api_basic.add_resource(Login, "/login")

from oioi.view.ranking import Ranking
api_basic.add_resource(Ranking, "/store/ranking")

from oioi.view.store import Store
api_basic.add_resource(Store, "/<store_id>")

from oioi.view.review import StoreReview
api_basic.add_resource(StoreReview, "/<store_id>/review")

from oioi.view.review import ProductReview
api_basic.add_resource(ProductReview, "/<store_id>/review/product")

from oioi.view.enrollment import EnrollmentStore
api_basic.add_resource(EnrollmentStore, "/store")

from oioi.view.enrollment import EnrollmentStoreProduct
api_basic.add_resource(EnrollmentStoreProduct, "/<store_id>/product")
