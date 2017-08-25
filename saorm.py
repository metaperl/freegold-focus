# coding: utf-8
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

engine = create_engine(
    'mysql+pymysql://root:m0ney123@localhost/focus',
    echo=True
)


class Affiliate(Base):
    __tablename__ = 'affiliate'

    kb_id = Column(String(128), primary_key=True)
    gfg = Column(Integer)
    kbuk_id = Column(Integer)
    lttw_id = Column(String(128))
    name = Column(String(128), nullable=False)
    number = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    pic = Column(String(1024), nullable=False)
    skype = Column(String(128))
