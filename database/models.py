from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

from database.database import Base


class AviatorHistory(Base):
    __tablename__ = "aviator_history"

    id = Column(Integer, primary_key=True)

    multiplier = Column(Float)

    created_at = Column(DateTime, default=datetime.utcnow)


class MinesHistory(Base):
    __tablename__ = "mines_history"

    id = Column(Integer, primary_key=True)

    board = Column(String)

    mines = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)