from main import db
from models.Artist import Artist
from flask import Blueprint, jsonify, abort, request
from schemas.ArtistSchema import artist_schema, artists_schema

artist = Blueprint("artist", __name__, url_prefix="/artist")

@artist.route("/", methods=["GET"])
def artist_index():
    return jsonify(artists_schema.dump(Artist.query.all()))

@artist.route("/<int:id>", methods=["GET"])
def artist_retrive(id):
    return jsonify(artist_schema.dump(Artist.query.get(id)))

@artist.route("/", methods=["POST"])
@auth_decorator
def artist_create():
    artist_fields = artist_schema.load(request.json)

    new_artist = Artist()
    new_artist.name = artist_fields["name"]

    db.session.add(new_artist)
    db.session.commit()

    return jsonify(artist_schema.dump(new_artist))

@artist.route("/<int:id>", methods=["PUT", "PATCH"])
@auth_decorator
def artist_update(id):
    artist_fields = artist_schema.load(request.json)

    artist = Artist.query.filter_by(id=id).update(artist_fields)

    if not artist:
        return abort(400)
    
    db.session.commit()

    return jsonify(artist_schema.dump(artist))
