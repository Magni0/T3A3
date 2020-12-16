from main import ma
from models.Tracks import Tracks
from schemas.ArtistSchema import ArtistSchema
from marshmallow.validate import Length

class TrackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tracks
    
    trackname = ma.String()
    artist = ma.Nested(ArtistSchema)
    trackurl = ma.String()

track_schema = TrackSchema()
tracks_schema = TrackSchema(many=True)