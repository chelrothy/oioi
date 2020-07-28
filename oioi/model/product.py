from sqlalchemy import Column, String, Integer, ForeignKey

from model import Base


class Product(Base):
    __tablename__ = 'product'
    _table_args_ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    picture = Column(String(100))
    store_id = Column(ForeignKey("store.id"), nullable=False)
