from main import db
from flask import Blueprint, request, jsonify, abort
from models.Moods import Moods
from schemas.MoodSchema import mood_schema
from flask_jwt_extended import jwt_required
from services.auth_decorator import auth_decorator

mood = Blueprint("mood", __name__, url_prefix="/tracks/<int:id>/moods")

@mood.route("/", methods=["GET"])
def retrive_moods(id):
    # Retrives all moods of track
    
    return jsonify(mood_schema.dump(Moods.query.get(id)))

@mood.route("/add", methods=["POST"])
def increment_mood(id):
    mood_fields = mood_schema.load(request.json)

    if len(mood_fields) != 1:
        return abort(400, description="More than one mood in request")

    for mood in mood_fields:
        mood = mood
    
    # tracks id is the same as moods id
    moods = Moods.query.filter_by(id=id)
    mood_dict = mood_schema.dump(moods[0])

    mood_num = mood_dict[mood]
    mood_fields[mood] = mood_num + 1

    moods.update(mood_fields)
    db.session.commit()

    return jsonify(mood_schema.dump(moods[0]))

@mood.route("/clear", methods=["DELETE"])
def clear_moods(id):
    # Sets all moods of a track to 0
    moods = Moods.query.filter_by(id=id)
    mood_json = mood_schema.dump(moods[0]) 

    mood_json['amusement'] = 0
    mood_json['joy'] = 0
    mood_json['beauty'] = 0
    mood_json['relaxation'] = 0
    mood_json['sadness'] = 0
    mood_json['dreaminess'] = 0
    mood_json['triumph'] = 0
    mood_json['anxiety'] = 0
    mood_json['scariness'] = 0
    mood_json['annoyance'] = 0
    mood_json['defiance'] = 0
    mood_json['feelingpumped'] = 0
    
    moods.update(mood_json)
    db.session.commit()

    return jsonify(mood_schema.dump(moods[0]))
