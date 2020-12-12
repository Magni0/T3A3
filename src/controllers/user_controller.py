from models.User import User
from schemas.UserSchema import user_schema
from main import db, bcrypt
from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import create_access_token
from datetime import timedelta

user = Blueprint("user", __name__, url_prefix="/userprofile")

@user.route("/register", methods=["POST"])
def user_register():
    user_fields = user_schema.load(request.json)

    user = User.query.filter_by(email=user_fields["email"]).first()

    if user:
        return abort(400, description="Email already registered to an account")

    user = User()
    user.displayname = user_fields["displayname"]
    user.username = user_fields["username"]
    user.email = user_fields["email"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")

    db.session.add(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))

@user.route("/login", methods=["GET"])
def user_login():
    user_fields = user_schema.load(request.json)

    try:
        user = User.query.filter_by(email=user_fields["email"]).first()
    except:
        user = User.query.filter_by(username=user_fields["username"]).first()

    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Inccorrect email/username or password")
    
    access_token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))

    return jsonify({"token": access_token})