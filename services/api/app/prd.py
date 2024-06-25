from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .settings import Base


class Prd(Base):
    __tablename__ = 'prd'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
