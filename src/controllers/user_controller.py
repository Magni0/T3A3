from models.User import User
from schemas.UserSchema import user_schema
from main import db, bcrypt
from flask import Blueprint, request, jsonify, abort

user = Blueprint("user", __name__, url_prefix="/userprofile")

@user.route("/register", methods=["POST"])
def user_register():
    pass

@user.route("/login", methods=["GET"])
def user_login():
    pass