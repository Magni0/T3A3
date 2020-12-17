from main import ma
from models.Moods import Moods

class MoodSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Moods

    amusement = ma.Integer()
    joy = ma.Integer()
    beauty = ma.Integer()
    relaxation = ma.Integer()
    sadness = ma.Integer()
    dreaminess = ma.Integer()
    triumph = ma.Integer()
    anxiety = ma.Integer()
    scariness = ma.Integer()
    annoyance = ma.Integer()
    defiance = ma.Integer()
    feelingpumped = ma.Integer()

mood_schema = MoodSchema()
moods_schema = MoodSchema(many=True)
