from main import db

class Tracks(db.Model):
    __tablename__ = "tracks"

    id = db.Column(db.String(), primary_key=True)
    trackname = db.Column(db.String(), nullable=False) 
    artist = db.Column(db.String(), ForeignKey("Artist.id"))
    trackurl = db.Column(db.String(), nullable=False)