from models.User import User
from schemas.UserSchema import user_schema
from main import db, bcrypt
from flask import Blueprint, request, jsonify, abort

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
    pass