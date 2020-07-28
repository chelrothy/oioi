from sqlalchemy import Column, String, Integer, DATETIME, ForeignKey

from oioi.model import Base


class ProductReview(Base):
    __tablename__ = 'product_review'
    _table_args_ = {'mysql_collate': 'utf8_general_ci'}

    product_review_id = Column(Integer, primary_key=True)
    content = Column(String(200), nullable=False)
    score = Column(Integer, nullable=False)
    datetime = Column(DATETIME, nullable=False)
    reviewer = Column(ForeignKey("user.id"), nullable=False)
    product_id = Column(ForeignKey("product.id"), nullable=False)
