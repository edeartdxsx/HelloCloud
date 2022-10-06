### crud.py ###
from datetime import datetime
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine
import yaml
from configs import DATABASE_URI, f_yam 
from models import Base, Book

engine = create_engine (DATABASE_URI)

Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        print('Error')
        raise
    finally:
        session.close()