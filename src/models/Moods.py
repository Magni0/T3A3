from main import db

class Moods(db.Model):
    __tablename__ = "moods"

    id = db.Column(db.String(), primary_key)
    amusement = db.Column(db.Integer)
    joy = db.Column(db.Integer)
    beauty = db.Column(db.Integer)
    relaxation = db.Column(db.Integer)
    sadness = db.Column(db.Integer)
    dreaminess = db.Column(db.Integer)
    triumph = db.Column(db.Integer)
    anxiety = db.Column(db.Integer)
    scariness = db.Column(db.Integer)
    annoyance = db.Column(db.Integer)
    defiance = db.Column(db.Integer)
    feelingpumped = db.Column(db.Integer)