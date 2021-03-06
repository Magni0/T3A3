from main import db
from flask import Blueprint
from random import choice
from main import bcrypt
import psycopg2
from psycopg2.extras import RealDictCursor
import json

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
    
    tables = ["userprofile", "tracks", "moods", "images", "artists"]
    
    dump = {}

    host = str(input("host[localhost]: ") or "localhost")
    database = str(input("database[postgres]: ") or "postgres")
    user = str(input("user[postgres]: ") or "postgres")
    password = input("password: ")

    connection = psycopg2.connect(
        database=database,
        user=user,
        password=password,
        host=host
    )

    cursor = connection.cursor(cursor_factory=RealDictCursor)

    for table in tables:
        cursor.execute(f"SELECT * FROM {table}")
        data = cursor.fetchall()
        dump[table] = data

    dump_path = input("Dump Path: ")

    with open(f"{dump_path}/database_dump.json", "w") as f:
        f.write(json.dumps(dump, indent=4))

@db_commands.cli.command("seed")
def seed_tables():
    
    # User
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

    # Artist
    artists = []
    for i in range(10):
        artist = Artist()
        artist.name = f"TestArtistName{i}"
        db.session.add(artist)
        artists.append(artist)
    
    db.session.commit()
    print("Seeded Table: artist")

    # Image
    for i in range(20):
        image = Image()
        image.url = f"TestURL{i}"
        image.height = choice(range(600, 1200))
        image.width = choice(range(600, 1200))
        db.session.add(image)
    
    db.session.commit()
    print("Seeded Table: images")

    def moods_table_creation():
        moods = Moods()

        moods.amusement = choice(range(1, 101))
        moods.joy = choice(range(1, 101))
        moods.beauty = choice(range(1, 101))
        moods.relaxation = choice(range(1, 101))
        moods.sadness = choice(range(1, 101))
        moods.dreaminess = choice(range(1, 101))
        moods.triumph = choice(range(1, 101))
        moods.anxiety = choice(range(1, 101))
        moods.scariness = choice(range(1, 101))
        moods.annoyance = choice(range(1, 101))
        moods.defiance = choice(range(1, 101))
        moods.feelingpumped = choice(range(1, 101))

        db.session.add(moods)
        db.session.commit()
        return moods

    # Tracks
    for i in range(30):
        track = Tracks()
        track.trackname = f"TestTrackName{i}"
        track.artist_id = choice(artists).id
        track.moods_id = moods_table_creation().id
        track.trackurl = f"TestTrackURL{i}"
        db.session.add(track)
    
    db.session.commit()
    print("Seeded Table: tracks")
    