# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Affiliate(Base):
    __tablename__ = 'affiliate'

    id = Column(Integer, primary_key=True)
    gfg = Column(Integer)
    kbuk_id = Column(Integer)
    lttw_id = Column(String(128))
    name = Column(String(128), nullable=False)
    number = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    pic = Column(String(1024), nullable=False)
    skype = Column(String(128))
