#autogenerated by sqlautocode

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation

engine = create_engine('postgres://metaperl:m0ney123@localhost/focus')
DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata
metadata.bind = engine

try:
    from sqlalchemy.dialects.postgresql import *
except ImportError:
    from sqlalchemy.databases.postgres import *
class Affiliate(DeclarativeBase):
    __tablename__ = 'affiliate'

    __table_args__ = {}

    #column definitions
    email = Column(u'email', VARCHAR(length=128), nullable=False)
    gfg = Column(u'gfg', BOOLEAN())
    id = Column(u'id', VARCHAR(length=128), primary_key=True, nullable=False)
    kbuk_id = Column(u'kbuk_id', INTEGER())
    lttw_id = Column(u'lttw_id', VARCHAR())
    name = Column(u'name', VARCHAR(length=128), nullable=False)
    number = Column(u'number', VARCHAR(length=128), nullable=False)
    pic = Column(u'pic', VARCHAR(length=512))
    skype = Column(u'skype', VARCHAR(length=128))

    #relation definitions


#example on how to query your Schema
from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)()
objs = session.query(Affiliate).all()
print 'All Affiliate objects: %s'%objs
