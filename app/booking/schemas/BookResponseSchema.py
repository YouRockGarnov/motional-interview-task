import marshmallow
from app.booking.schemas.PointSchema import PointSchema


class BookResponseSchema(marshmallow.Schema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    car_id = marshmallow.fields.Integer()
    total_time = marshmallow.fields.Integer()
