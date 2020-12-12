from main import ma
from models.User import User
from marshmallow.validate import Length

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_only = ["password"]

    displayname = ma.String(required=True, validate=Length(min=1))
    email = ma.String(required=True, validate=Length(min=1))
    username = ma.String(required=True, validate=Length(min=1))
    password = ma.String(required=True, validate=Length(min=8))

user_schema = UserSchema()
users_schema = UserSchema(many=True)