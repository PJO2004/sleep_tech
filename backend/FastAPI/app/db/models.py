from .database import Base
from sqlalchemy import Column, Integer, String, Numeric


class test(Base):
	__tablename__ = "test"

	Index = Column(Integer, primary_key=True, index=True)
	Date = Column(String(15), unique=False)
	Point = Column(Integer, unique=False)
	Average_temperature_ = Column(Numeric, unique=False)
	Lowest_temperature_ = Column(Numeric, unique=False)
	Maximum_temperature_ = Column(Numeric, unique=False)
