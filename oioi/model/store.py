from sqlalchemy import Column, String, Integer

from oioi.model import Base


class Store(Base):
    __tablename__ = 'store'
    _table_args_ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
    score = Column(Integer, nullable=True)
    average_score = Column(Integer, nullable=False)
    ranking = Column(Integer, nullable=True)
    picture = Column(String(200), nullable=False)
