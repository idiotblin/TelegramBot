from sqlalchemy import Column, Integer, String
from database import Base


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    num = Column(Integer)
    name = Column(String, default=True)
    text = Column(String, default=True)
