import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def4 import Items

engine = create_engine('sqlite:///items.db', echo=True)

#Create a Session
Session = sessionmaker(bind=engine)
session = Session()

#Create an Artist
new1 = Items("iPod", "28th & Colorado", "Bob Barker", 40, "303-555-5555", "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRm3aY-sEAnXQMM-hcr9jmxiOCwE2Xpcxc-VKrSoozAQpkDasbMbw")
new2 = Items("MacBook Pro", "Pearl & Walnut", "Sam Parkers", 120, "720-888-8888", "http://i.i.cbsi.com/cnwk.1d/i/tim/2012/06/12/Macbook_Pro_2012_with_Retina_Display_35331572_05_620x433.jpg")
new3 = Items("Yellow Umbrella", "20th & Colorado", "Wendy Burgers", 0, "303-456-7899", "http://3.bp.blogspot.com/-85uusYei7_Y/TdKyIlHcU3I/AAAAAAAAEIs/MIzpy3kHi3o/s400/ist2_4271412-yellow-umbrella.jpg")
new4 = Items("Left Shoe", "Boulder High School", "Tupac", 150, "780-239-2222", "https://static.squarespace.com/static/51b3dc8ee4b051b96ceb10de/51ce6099e4b0d911b4489b79/51ce617be4b0d911b4495a54/1362790736827/1000w/DSC_0200.jpg")
new5 = Items("Gnome", "Arapahoe & Broadway", "Ronald Weasley", 5, "920-222-3333", "http://img0.etsystatic.com/000/0/5294952/il_fullxfull.195769930.jpg?ref=l2")
new6 = Items("iPad", "17th & College", "Christy Sports", 80, "303-303-3030", "http://i0.wp.com/hypebeast.com/image/2013/01/apple-to-introduce-a-128gb-ipad-with-retina-display-1.jpg?w=1410")
new7 = Items("My Homework", "13th & University", "Stephanie Bickmore", 20, "720-720-7202", "http://upload.wikimedia.org/wikipedia/commons/1/15/Homework_-_vector_maths.jpg")
new8 = Items("Grey Jacket", "14th & Cascade", "Kristin Burner", 0, "303-888-9999", "http://www.selectism.com/news/wp-content/uploads/2009/11/nom-de-guerre-grey-jacket-wings-horns-00.jpg")
new9 = Items("Pink Poncho", "15th & Broadway", "Ben Dover", 30, "455-566-7788", "http://img.inkashandcrafts.com/wp-content/uploads/2011/05/Inkas-Pink-Woman-Poncho_1.jpg")
new10 = Items("Top Hat", "12th & Canyon", "Abraham Lincoln", 100, "100-100-1776", "http://upload.wikimedia.org/wikipedia/commons/3/38/Collapsible_top_hat_IMGP9662.jpg")

#Add the record to the session object
session.add(new1)
session.add(new2)
session.add(new3)
session.add(new4)
session.add(new5)
session.add(new6)
session.add(new7)
session.add(new8)
session.add(new9)
session.add(new10)

session.commit()
