from main import db
from models.Artist import Artist

class ArtistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Artist

    name = ma.String()

artist_schema = ArtistSchema()
artists_schema = ArtistSchema(many=True)