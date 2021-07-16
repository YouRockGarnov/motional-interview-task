from app.booking.schemas.BookJsonSchema import BookJsonSchema
from app.booking.schemas.BookResponseSchema import BookResponseSchema
from app.managers.car_manager import CarManager
from flask_smorest import Blueprint
from flask.views import MethodView

from app.utils.Point import Point

blueprint = Blueprint('Bookings', 'Bookings')


@blueprint.route('/book')
class BookResource(MethodView):
    @blueprint.arguments(BookJsonSchema)
    def post(self, json_body):
        result = CarManager.book_nearest_available_car(source=Point(**json_body['source']),
                                                       destination=Point(**json_body['destination']))
        return BookResponseSchema().load(result)


@blueprint.route('/tick')
class TickResource(MethodView):
    @blueprint.response(200)
    def post(self):
        CarManager.tick()


@blueprint.route('/reset')
class ResetResource(MethodView):
    @blueprint.response(200)
    def put(self):
        CarManager.reset()
