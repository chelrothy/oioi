from sqlalchemy import Column, String, Integer, ForeignKey, DATETIME

from model import Base


class StoreReview(Base):
    __tablename__ = 'store_review'
    _table_args_ = {'mysql_collate': 'utf8_general_ci'}

    store_review_id = Column(Integer, primary_key=True)
    store_id = Column(ForeignKey("store.id"), nullable=False)
    content = Column(String(200))
    score = Column(Integer, nullable=False)
    datetime = Column(DATETIME, nullable=False)
    reviewer = Column(ForeignKey("user.id"), nullable=False)
