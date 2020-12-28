from main import db
from models.Artist import Artist
from flask import Blueprint, jsonify, abort, request
from schemas.ArtistSchema import artist_schema

artist = Blueprint("artist", __name__, url_prefix="/artist")

@artist.route("/", methods=["GET"])
def artist_index():
    pass

@artist.route("/<int:id>", methods=["GET"])
def artist_retrive():
    pass

@artist.route("/<int:id>", methods=["POST"])
def artist_create():
    pass

@artist.route("/<int:id>", methods=["PUT", "PATCH"])
def artist_update():
    pass

@artist.route("/<int:id>", methods=["DELETE"])
def artist_delete():
    pass