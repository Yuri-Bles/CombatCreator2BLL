from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Designer(Base):
    __tablename__ = "Designer"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)

class DraftStat(Base):
    __tablename__ = "SystemStat"

    ID = Column(Integer, primary_key=True, autoincrement=True)
    SystemID = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    default_value = Column(Numeric, nullable=False)
    min_value = Column(Numeric, nullable=False)
    max_value = Column(Numeric, nullable=False)
