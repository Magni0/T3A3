from main import db
from models.Tracks import Tracks

class Artist(db.Model):
    __tablename__="artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    tracks = db.relationship("Tracks", uselist=False, backref="artists")