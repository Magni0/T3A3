from main import db
from flask import Blueprint

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

@db_commands.cli.command("seed-user")
def seed_tables_user():
    from main import bcrypt
    from models.User import User

    users = []

    for i in range(10):
        user = User()
        user.displayname = f"testuser{i}"
        user.email = f"testemail{i}@test.com"
        user.username = f"testusername{i}"
        user.password = bcrypt.generate_password_hash("testpassword").decode("utf-8")
        db.session.add(user)
        users.append(user)
    
    db.session.commit()

@db_commands.cli.command("seed-images")
def seed_tables_images():
    from models.Image import Image
    from random import choice

    for i in range(20):
        image = Image()
        image.url = f"testurl{i}.com"
        image.height = choice(range(600, 1200))
        image.width = choice(range(600, 1200))
        db.session.add(image)
    
    db.session.commit()

@db_commands.cli.command("seed-moods")
def seed_tables_moods():
    pass

@db_commands.cli.command("seed-tracks")
def seed_tables_tracks():
    pass

@db_commands.cli.command("seed-artist")
def seed_tables_artist():
    pass

@db_commands.cli.command("seed")
def seed_tables():
    pass