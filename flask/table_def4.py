# table_def.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///items.db', echo=True)
Base = declarative_base()
 
class Items(Base):
	""""""
	__tablename__ = "items"
 
	id = Column(Integer, primary_key=True)
	name = Column(String)
	location = Column(String)
	owner = Column(String)
	reward = Column(Integer)
	contact = Column(String)
	pic = Column(String)
 
 
	def __init__(self, name, location, owner, reward, contact, pic):
		""""""

		self.name = name
		self.location = location
		self.owner = owner
		self.reward = reward
		self.contact = contact
		self.pic = pic

Base.metadata.create_all(engine)