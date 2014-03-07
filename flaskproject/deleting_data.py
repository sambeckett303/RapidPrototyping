# deleting_data.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist

engine = create_engine('sqlite:///mymusic.db', echo=True)
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
res = session.query(Artist).filter(Artist.name=="MXPX").first()
res2 = session.query(Artist).filter(Artist.name=="Newsboys").first()
res3 = session.query(Artist).filter(Artist.name=="Kutless").first()
res4 = session.query(Artist).filter(Artist.name=="Thousand Foot Krutch").first()
 
session.delete(res)
session.delete(res2)
session.delete(res3)
session.delete(res4)
session.commit()