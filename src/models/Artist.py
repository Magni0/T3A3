from main import db

class Artist(db.Model):
    __tablename__ = "artist"

    id = db.Column(db.String(), primary_key=True)
    tracks = relationship("Track", uselist=False, backref="artist")