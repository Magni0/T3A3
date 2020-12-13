from main import ma
from models.Tracks import Tracks
from schemas.ArtistSchema import ArtistSchema
from marshmallow.validate import Length

class TrackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tracks
    
    trackname = ma.String(required=True, validate=Length(min=1))
    artist = ma.Nested(ArtistSchema)
    trackurl = ma.String(required=True, validate=Length(min=1))

track_schema = TrackSchema()
tracks_schema = TrackSchema(many=True)