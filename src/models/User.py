from main import db
from sqlalchemy import Sequence

class User(db.Model):
    __tablename__="userprofile"

    id = db.Column(db.Integer, Sequence("userprofile_id_seq"), primary_key=True,)
    displayname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
