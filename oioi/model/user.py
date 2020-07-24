from sqlalchemy import Column, String

from oioi.model import Base


class User(Base):
    __tablename__ = 'user'
    _table_args_ = {'mysql_collate': 'utf8_general_ci'}

    id = Column(String(100), primary_key=True)
    password = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
