from main import db

class Moods(db.Model):
    __tablename__="moods"

    id = db.Column(db.Integer, primary_key=True)
    amusement = db.Column(db.Integer, default=0)
    joy = db.Column(db.Integer, default=0)
    beauty = db.Column(db.Integer, default=0)
    relaxation = db.Column(db.Integer, default=0)
    sadness = db.Column(db.Integer, default=0)
    dreaminess = db.Column(db.Integer, default=0)
    triumph = db.Column(db.Integer, default=0)
    anxiety = db.Column(db.Integer, default=0)
    scariness = db.Column(db.Integer, default=0)
    annoyance = db.Column(db.Integer, default=0)
    defiance = db.Column(db.Integer, default=0)
    feelingpumped = db.Column(db.Integer, default=0)