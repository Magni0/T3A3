from main import db

class User(db.Model):
    __tablename__="userprofile"

    id = db.Column(db.Integer, primary_key=True,)
    displayname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
