from main import db
from models.Tracks import Tracks

class Moods(db.Model):
    __tablename__="moods"

    id = db.Column(db.Integer, primary_key=True)
    amusement = db.Column(db.Integer, default=0, nullable=False)
    joy = db.Column(db.Integer, default=0, nullable=False)
    beauty = db.Column(db.Integer, default=0, nullable=False)
    relaxation = db.Column(db.Integer, default=0, nullable=False)
    sadness = db.Column(db.Integer, default=0, nullable=False)
    dreaminess = db.Column(db.Integer, default=0, nullable=False)
    triumph = db.Column(db.Integer, default=0, nullable=False)
    anxiety = db.Column(db.Integer, default=0, nullable=False)
    scariness = db.Column(db.Integer, default=0, nullable=False)
    annoyance = db.Column(db.Integer, default=0, nullable=False)
    defiance = db.Column(db.Integer, default=0, nullable=False)
    feelingpumped = db.Column(db.Integer, default=0, nullable=False)
    track = db.relationship("Tracks", uselist=False, backref="mood")