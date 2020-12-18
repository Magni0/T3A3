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
def increment_mood(track_id):
    # mood_fields = mood_schema.load(request.json)
    
    # # tracks id is the same as moods id
    # moods = Moods.query.get(track_id)

    pass

@mood.route("/clear", methods=["DELETE"])
def clear_moods(track_id):
    # Sets all moods of a track to 0
    
    pass
