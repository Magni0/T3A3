from main import db
from flask import Blueprint, request, jsonify, abort
from models.Tracks import Tracks
from schemas.TrackSchema import track_schema, tracks_schema
from flask_jwt_extended import jwt_required
from services.auth_decorator import auth_decorator

track = Blueprint("track", __name__, url_prefix="/tracks")

@track.route("/", methods=["GET"])
def track_index():
    # Retrives all tracks

    return jsonify(tracks_schema.dump(Tracks.qurey.all()))

@track.route("/track/<int:id>", methods=["GET"])
def track_retrive(id):
    # Retrives single track

    return jsonify(track_schema.dump(Tracks.query.get(id)))

@track.route("/track", methods=["POST"])
@jwt_required
@auth_decorator
def track_create(user=None):
    # Creates a track
    
    track_fields = track_schema.load(request.json)

    new_track = Tracks()
    new_track.trackname = track_fields["trackname"]
    #add artist_id
    #add moods_id
    new_track.trackurl = track_fields["trackurl"]

    user.track.append(new_track) # may be broken

    db.session.add(new_track)
    db.session.commit()

    return jsonify(track_schema.dump(new_track))

@track.route("/track/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@auth_decorator
def track_update(id, user=None):
    # Updates a track

    track_fields = track_schema.load(request.id)

    # track = Tracks.query.filter_by(id=id)

@track.route("/track/<int:id>", methods=["DELETE"])
@jwt_required
@auth_decorator
def track_delete(id, user=None):
    # Deletes a track
    
    track = Tracks.query.get(id)

    if not track:
        return abort(400)
    
    db.session.delete(track)
    db.session.commit()

    return jsonify(track_schema.dump(track))
