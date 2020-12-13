from main import ma
from models.Moods import Moods

class MoodSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Moods

    amusement = ma.Integer(required=True)
    joy = ma.Integer(required=True)
    beauty = ma.Integer(required=True)
    relaxation = ma.Integer(required=True)
    sadness = ma.Integer(required=True)
    dreaminess = ma.Integer(required=True)
    triumph = ma.Integer(required=True)
    anxiety = ma.Integer(required=True)
    scariness = ma.Integer(required=True)
    annoyance = ma.Integer(required=True)
    defiance = ma.Integer(required=True)
    feelingpumped = ma.Integer(required=True)

mood_schema = MoodSchema()
moods_schema = MoodSchema(many=True)