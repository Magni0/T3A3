from main import db

class Tracks(db.Model):
    __tablename__="tracks"

    id = db.Column(db.Integer, primary_key=True)
    trackname = db.Column(db.String(), nullable=False) 
    artist = db.Column(db.Integer, db.ForeignKey("artists.id"))
    trackurl = db.Column(db.String(), nullable=False)