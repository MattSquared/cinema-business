from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Engine = create_engine("sqlite:///cache.db", convert_unicode=True)
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=Engine))
Base = declarative_base()
Base.query = Session.query_property()


def start_db():
    Base.metadata.create_all(bind=Engine)


def clean_db():
    Session.remove()

