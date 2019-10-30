from sqlalchemy import Column, Integer, Float, DateTime
from app import db


class Measurement(db.Model):


    __tablename__ = 'measurement'

    id = Column(Integer, primary_key = True, autoincrement = True) 

    front_left_weel = Column(Float, nullable = False)
    front_right_weel = Column(Float, nullable = False)    
    back_left_weel = Column(Float, nullable = False)
    back_right_weel = Column(Float, nullable = False)
    servo_angle = Column(Float,nullable = False)
    timestamp = Column(DateTime(timezone=True),

                       nullable=False,

                       server_default='now()')