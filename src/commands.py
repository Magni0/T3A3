from main import db
from flask import Blueprint
from random import choice
from main import bcrypt

from models.User import User
from models.Tracks import Tracks
from models.Artist import Artist
from models.Image import Image


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
        track.artist = choice(artists).id
        track.trackurl = f"TestTrackURL{i}"
        db.session.add(track)
    
    db.session.commit()
    print("Seeded Table: tracks")
