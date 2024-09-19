from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from model import Base

class Glucose(Base):
    __tablename__ = 'glucose'

    id = Column("pk_glucose", Integer, primary_key=True)
    name = Column(String(60), unique=False)
    glucose = Column(Float)

    # The date will always be taken as the default value to facilitate registration for those who are not familiar with it.
    insertion_date = Column(DateTime, default= datetime.now())

    def __init__(self, name:str, glucose:float):       
        """
        create a glucose log

        Arguments:
            name: Person's name
            glucose: measured glucose value
            insertion_date: date when it was inserted
        """

        self.name = name
        self.glucose = glucose