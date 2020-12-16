from main import db
from flask import Blueprint, request, jsonify, abort
from models.Tracks import Tracks
from schemas.TrackSchema import track_schema
from flask_jwt_extended import jwt_required
from services.auth_decorator import auth_decorator

track = Blueprint("track", __name__, url_prefix="/tracks")

@track.route("/", methods=["GET"])
@jwt_required
@auth_decorator
def track_index(user=None):
    pass

@track.route("/track/<int:id>", methods=["GET"])
@jwt_required
@auth_decorator
def track_retrive(id, user=None):
    pass

@track.route("/track", methods=["POST"])
@jwt_required
@auth_decorator
def track_create(user=None):
    pass

@track.route("/track/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@auth_decorator
def track_update(id, user=None):
    pass

@track.route("/track/<int:id>", methods=["DELETE"])
@jwt_required
@auth_decorator
def track_delete(id, user=None):
    pass
