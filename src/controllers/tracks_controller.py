from main import db
from flask import Blueprint, request, jsonify, abort, render_template
from models.Tracks import Tracks
from models.Moods import Moods
from schemas.TrackSchema import track_schema, tracks_schema
from flask_jwt_extended import jwt_required
from services.auth_decorator import auth_decorator
from services.delete_record_decorator import delete_record_decorator

track = Blueprint("track", __name__, url_prefix="/tracks")

@track.route("/", methods=["GET"])
def track_index():
    # Retrives all tracks

    # return jsonify(tracks_schema.dump(Tracks.query.all()))
    return render_template("tracks_index.html", tracks=Tracks.query.all())

@track.route("/<int:id>", methods=["GET"])
def track_retrive(id):
    # Retrives single track

    return jsonify(track_schema.dump(Tracks.query.get(id)))

@track.route("/create", methods=["POST"])
@auth_decorator
def track_create():
    # Creates a track
    
    track_fields = track_schema.load(request.json)

    new_mood = Moods()
    db.session.add(new_mood)
    db.session.commit()

    new_track = Tracks()
    new_track.trackname = track_fields["trackname"]
    new_track.moods_id = new_mood.id
    new_track.trackurl = track_fields["trackurl"]

    db.session.add(new_track)
    db.session.commit()

    return jsonify(track_schema.dump(new_track))

@track.route("/<int:id>", methods=["PUT", "PATCH"])
@auth_decorator
def track_update(id, user=None):
    # Updates a track

    track_fields = track_schema.load(request.json)

    track = Tracks.query.filter_by(id=id).update(track_fields)

    if not track:
        return abort(400)

    db.session.commit()

    return jsonify(track_schema.dump(track))
    

@track.route("/<int:id>", methods=["DELETE"])
@delete_record_decorator
@auth_decorator
def track_delete(id, user=None):
    # Deletes a track

    track = Tracks.query.get(id)
    mood = Moods.query.get(id)

    if not track:
        return abort(400)

    db.session.delete(mood)
    db.session.delete(track)
    db.session.commit()

    return jsonify(track_schema.dump(track))
