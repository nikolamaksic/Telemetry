from sqlalchemy import Column, Integer, Float, DateTime, String
from app import db


class Parameters(db.Model):


    __tablename__ = 'parameters'

    id = Column(Integer, primary_key = True, autoincrement = True) 
    param1 = Column(String, nullable = False)
    timestamp = Column(DateTime(timezone=True),

                       nullable=False,

                       server_default='now()')