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

@db_commands.cli.command("seed")
def seed_tables():
    pass