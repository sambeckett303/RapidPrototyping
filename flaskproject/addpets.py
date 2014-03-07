import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def2 import Pets

engine = create_engine('sqlite:///pets.db', echo=True)

#Create a Session
Session = sessionmaker(bind=engine)
session = Session()

#Create an Artist
new_pet = Pets("Ralphie", "Male", 21, "Very Slow")
new_pet2 = Pets("Crawly", "Female", 26, "Moderately Slow")
new_pet3 = Pets("Bob", "Male", 19, "Fastly Slow")
new_pet4 = Pets("Wendy", "Female", 28, "Turtle Slow")
new_pet5 = Pets("James", "Male", 29, "Creeping")
new_pet6 = Pets("Sally", "Female", 18, "REALLY fast")
new_pet7 = Pets("Harry", "Male", 50, "Too Slow to Exist")
new_pet8 = Pets("Kristin", "Female", 42, "Somewhat Slow")
new_pet9 = Pets("Samson", "Male", 33, "What?")
new_pet10 = Pets("Shelly", "Female", 35, "Sluggish")

#Add the record to the session object
session.delete(new_pet)
session.delete(new_pet2)
session.add(new_pet3)
session.add(new_pet4)
session.add(new_pet5)
session.add(new_pet6)
session.add(new_pet7)
session.add(new_pet8)
session.add(new_pet9)
session.add(new_pet10)

session.commit()
