from main import db
from models.Tracks import Tracks

class Artist(db.Model):
    __tablename__ = "artist"

    id = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    tracks = relationship("Tracks", uselist=False, backref="name")