# from datetime import datetime

# from sqlalchemy import Column, DateTime
# from sqlalchemy.ext.declarative import as_declarative, declared_attr


# @as_declarative()
# class Base:
#     __abstract__ = True
#     __name__: str

#     # Generate __tablename__ automatically
#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()


# class BareBaseModel(Base):
#     __abstract__ = True

#     # id = Column(Integer, primary_key=True, autoincrement=True)
#     created_date_time = Column(DateTime, default=datetime.now, nullable=False)
#     last_updated_date_time = Column(
#         DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
#     )

#     @staticmethod
#     def default_datetime():
#         return datetime.now()
