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
        """
        Pick the nearest available car to the customer location and return the total time taken to travel
        from the current car location to customer location then to customer destination.
        """

        result = CarManager.book_nearest_available_car(source=Point(**json_body['source']),
                                                       destination=Point(**json_body['destination']))
        return BookResponseSchema().load(result)


@blueprint.route('/tick')
class TickResource(MethodView):
    @blueprint.response(200)
    def post(self):
        """
        Advance the service time stamp by 1 time unit.
        """

        CarManager.tick()


@blueprint.route('/reset')
class ResetResource(MethodView):
    @blueprint.response(200)
    def put(self):
        """
        Will reset all cars data back to the initial state regardless of cars that are currently booked.
        """

        CarManager.reset()
