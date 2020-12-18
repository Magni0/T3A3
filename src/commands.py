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

@db_commands.cli.command("check")
def check_id():
    last_record = db.session.query(User).order_by(User.id.desc()).first()
    print(resent_record.id)

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Deleted Tables")

@db_commands.cli.command(f"dump")
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

    dump_path = input("Type Dump Path: ")

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

    # Tracks
    for i in range(30):
        moods = Moods()
        track = Tracks()
        db.session.add(moods)
        db.session.commit()
        track.trackname = f"TestTrackName{i}"
        track.artist_id = choice(artists).id
        track.moods_id = moods.id
        track.trackurl = f"TestTrackURL{i}"
        db.session.add(track)
    
    db.session.commit()
    print("Seeded Table: tracks")
    