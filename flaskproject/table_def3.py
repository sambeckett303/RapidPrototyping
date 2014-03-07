# table_def.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///resorts.db', echo=True)
Base = declarative_base()
 
class Resorts(Base):
	""""""
	__tablename__ = "Resorts"
 
	id = Column(Integer, primary_key=True)
	name = Column(String)
	base = Column(Integer)
	peak = Column(Integer)
	runs = Column(Integer)
	parks = Column(Integer)
 
 
	def __init__(self, name, base, peak, runs, parks):
		""""""

		self.name = name
		self.base = base
		self.peak = peak
		self.runs = runs
		self.parks = parks

Base.metadata.create_all(engine)