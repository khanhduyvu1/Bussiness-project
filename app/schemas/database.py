from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from models import book, user


engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URL"), pool_size=3000, max_overflow=2000)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
def create_tables():
    try:
        list_tables = [user.User.__table__,
                      book.Book.__table__
                      ]
        Base.metadata.create_all(bind=engine, tables=list_tables)
        print("Tables created successfully.")
    except Exception as e:
        print("Error creating tables:", e)  

create_tables()  