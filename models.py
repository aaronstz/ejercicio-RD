from sqlalchemy import Column, Integer, String
from database import Base

class DataModel(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    field_1 = Column(String)
    author = Column(String)
    description = Column(String)
    my_numeric_field = Column(Integer)