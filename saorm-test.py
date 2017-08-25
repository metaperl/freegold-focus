
from sqlalchemy import create_engine

from saorm import Affiliate, engine

engine = create_engine(
    'mysql+pymysql://root:m0ney123@localhost/focus',
    echo=True
)


#example on how to query your Schema
from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)()
objs = session.query(Affiliate).all()
print 'All Affiliate objects: %s'%objs
