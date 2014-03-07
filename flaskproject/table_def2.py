# table_def.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///pets.db', echo=True)
Base = declarative_base()
 
class Pets(Base):
	""""""
	__tablename__ = "pets"
 
	id = Column(Integer, primary_key=True)
	name = Column(String)
	gender = Column(String)
	age = Column(Integer)
	speed = Column(String)
 
 
	def __init__(self, name, gender, age, speed):
		""""""

		self.name = name
		self.gender = gender
		self.age = age
		self.speed = speed

Base.metadata.create_all(engine)