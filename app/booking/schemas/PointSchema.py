import marshmallow


class PointSchema(marshmallow.Schema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    x = marshmallow.fields.Str(required=True)
    y = marshmallow.fields.Str(required=True)