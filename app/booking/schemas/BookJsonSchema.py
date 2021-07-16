import marshmallow
from app.booking.schemas.PointSchema import PointSchema


class BookJsonSchema(marshmallow.Schema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    source = marshmallow.fields.Nested(PointSchema, required=True)
    destination = marshmallow.fields.Nested(PointSchema, required=True)
