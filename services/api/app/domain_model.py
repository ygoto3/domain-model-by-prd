from sqlalchemy import Column, Integer, String
from .settings import Base


class DomainModel(Base):
    __tablename__ = 'domain_model'

    id = Column(Integer, primary_key=True)
    prd_id = Column(Integer)
    mermaid = Column(String)
