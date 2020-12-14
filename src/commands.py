from main import db
from flask import Blueprint
from random import choice
from main import bcrypt

from models.User import User
from models.Tracks import Tracks
from models.Artist import Artist
from models.Image import Image
from models.Moods import Moods


db_commands = Blueprint("db-c", __name__)

# these commands are for testing purposes only

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Created Tables")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Deleted Tables")

@db_commands.cli.command("dump")
def dump_tables():
    users = db.session.query(User).all()
    print("\nuserprofile")
    for user in users:
        print(f"id: {user.id} | displayname: {user.displayname} | email: {user.email} | username: {user.username}")

    tracks = db.session.query(Tracks).all()
    print("\ntracks")
    for track in tracks:
        print(f"id: {track.id} | trackname: {track.trackname} | artist_id: {track.artist_id} | trackurl: {track.trackurl}")

    artists = db.session.query(Artist).all()
    print("\nartists")
    for artist in artists:
        print(f"id: {artist.id} | name: {artist.name}")

    images = db.session.query(Image).all()
    print("\nimages")
    for image in images:
        print(f"id: {image.id} | url: {image.url} | height: {image.height} | width: {image.width}")

    moods = db.session.query(Moods).all()
    print("\nmoods")
    for mood in moods:
        print(f"id: {mood.id} | amusement: {mood.amusement} | joy: {mood.joy} | beauty: {mood.beauty} | relaxation: {mood.relaxation} | sadness: {mood.sadness} | dreaminess: {mood.dreaminess} | triumph: {mood.triumph} | anxiety: {mood.anxiety} | scariness: {mood.scariness} | annoyance: {mood.annoyance} | defiance: {mood.defiance} | feelingpumped: {mood.feelingpumped}")

@db_commands.cli.command("seed")
def seed_tables():
    for i in range(10):
        user = User()
        user.id = i
        user.displayname = f"testuser{i}"
        user.email = f"TestEmail{i}@test.com"
        user.username = f"TestUserName{i}"
        user.password = bcrypt.generate_password_hash("testpassword").decode("utf-8")
        db.session.add(user)
    
    db.session.commit()
    print("Seeded Table: user")

    artists = []

    for i in range(10):
        artist = Artist()
        artist.name = f"TestArtistName{i}"
        db.session.add(artist)
        artists.append(artist)
    
    db.session.commit()
    print("Seeded Table: artist")

    for i in range(20):
        image = Image()
        image.url = f"TestURL{i}"
        image.height = choice(range(600, 1200))
        image.width = choice(range(600, 1200))
        db.session.add(image)
    
    db.session.commit()
    print("Seeded Table: images")

    for i in range(30):
        track = Tracks()
        track.trackname = f"TestTrackName{i}"
        track.artist_id = choice(artists).id
        track.trackurl = f"TestTrackURL{i}"
        db.session.add(track)
    
    db.session.commit()
    print("Seeded Table: tracks")

    for i in range(5):
        moods = Moods()
        db.session.add(moods)
    
    db.session.commit()
    print("Seeded Table: moods")