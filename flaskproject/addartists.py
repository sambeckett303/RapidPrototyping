import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist

engine = create_engine('sqlite:///mymusic.db', echo=True)

#Create a Session
Session = sessionmaker(bind=engine)
session = Session()

#Create an Artist
new_artist = Artist("Rebelution")
new_artist.albums = [Album("Bright Side of Life", "Reggae", "Controlled Substance Sound Lab", "CD")]

#Add more albums
more_albums = [Album("Peace of Mind", "Reggae", "87 Music", "CD")]
new_artist.albums.extend(more_albums)

#Add the record to the session object
session.add(new_artist)
#commit
new_artist2 = Artist("Eminem")
new_artist2.albums = [Album("The Eminem Show", "Rap", "Shady Records", "CD")]
new_artist3 = Artist("Sum 41")
new_artist3.albums = [Album("Does This Look Infected?", "Punk", "Island Records", "CD")]
new_artist4 = Artist("Katy Perry")
new_artist4.albums = [Album("One of the Boys", "Pop", "Capitol Music Group", "CD")]
session.add(new_artist2)
session.add(new_artist3)
session.add(new_artist4)
session.commit()
