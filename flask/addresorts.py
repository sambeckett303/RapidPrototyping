import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def3 import Resorts

engine = create_engine('sqlite:///resorts.db', echo=True)

#Create a Session
Session = sessionmaker(bind=engine)
session = Session()

#Create an Artist
new1 = Resorts("Arapahoe Basin", 10780, 13050, 105, 2)
new2 = Resorts("Copper Mountain", 9712, 12313, 126, 2)
new3 = Resorts("Winter Park", 9000, 12060, 134, 1)



session.add(new1)
session.add(new2)
session.add(new3)

session.commit()
