import marshmallow


class PointSchema(marshmallow.Schema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    x = marshmallow.fields.Int(required=True)
    y = marshmallow.fields.Int(required=True)