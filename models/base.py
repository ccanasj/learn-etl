from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime
from datetime import datetime


EntityMeta = declarative_base()


class Base(EntityMeta):
    __abstract__ = True

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        unique=True,
    )

    created_on = Column(DateTime, default=datetime.now, nullable=False)
    updated_on = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
