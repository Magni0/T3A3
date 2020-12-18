from main import db
from flask import Blueprint, request, jsonify, abort
from models.Moods import Moods
from schemas.MoodSchema import mood_schema
from flask_jwt_extended import jwt_required
from services.auth_decorator import auth_decorator

mood = Blueprint("mood", __name__, url_prefix="/tracks/moods")

@mood.route("/track/<int:id>", methods=["GET"])
def retrive_moods(id):
    # Retrives all moods of track
    
    return jsonify(mood_schema.dump(Moods.query.get(id)))

@mood.route("track/<int:track_id>/add", methods=["POST"]) # need to add a str variable at end of path
def increment_mood(track_id):
    # Increments specified mood by 1 
    
    pass

@mood.route("track/<int:track_id>", methods=["DELETE"])
def clear_moods(track_id):
    # Sets all moods of a track to 0
    
    pass

@mood.route("track/<int:track_id>/clear", methods=["DELETE"])
def clear_mood(track_id):
    # Sets specified mood to 0
    
    pass
