from main import db

class Image(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, db.Sequence('images_id_seq'), primary_key=True)
    url = db.Column(db.String())
    height = db.Column(db.Integer)
    width = db.Column(db.Integer)
