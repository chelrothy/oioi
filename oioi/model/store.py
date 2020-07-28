from sqlalchemy import Column, String, Integer

from model import Base


class Store(Base):
    __tablename__ = 'store'
    _table_args_ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(200), nullable=False)
    average_price = Column(Integer, nullable=False)
    picture = Column(String(200), nullable=False)
    average_score = Column(Integer, nullable=True)
    ranking = Column(Integer, nullable=True)
