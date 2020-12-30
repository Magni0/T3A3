from main import db
from flask import Blueprint, request, jsonify, abort
from models.Moods import Moods
from schemas.MoodSchema import mood_schema
from flask_jwt_extended import jwt_required
from services.auth_decorator import auth_decorator

mood = Blueprint("mood", __name__, url_prefix="/tracks/<int:id>/moods")

@mood.route("/", methods=["GET"])
def moods_retrive(id):
    # Retrives all moods of track
    
    return jsonify(mood_schema.dump(Moods.query.get(id)))

@mood.route("/add", methods=["POST"])
def mood_increment(id):
    # increments a selected mood by 1
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
@auth_decorator
def moods_clear(id):
    # Sets all moods of a track to 0
    moods = Moods.query.filter_by(id=id)
    mood_json = mood_schema.dump(moods[0]) 

    for mood in mood_json:
        if mood == "id":
            continue
        else:
            mood_json[mood] = 0
    
    moods.update(mood_json)
    db.session.commit()

    return jsonify(mood_schema.dump(moods[0]))
