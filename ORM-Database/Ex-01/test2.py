from unicodedata import name
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

engine = create_engine('sqlite:///user.db', echo = False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user3   = User(name='user3', fullname='STEd Jones', nickname = 'STEd')
user4   = User(name='user4', fullname='WTEd Jones', nickname = 'WTEd')

session.add_all(user3,user4)
session.commit()