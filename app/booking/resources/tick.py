from app.booking.resources.BookingResourceBase import BookingResourceBase
from app.booking.schemas.BookJsonSchema import BookJsonSchema
from app.booking.schemas.BookResponseSchema import BookResponseSchema
from app.managers.car_manager import CarManager


@BookingResourceBase.blueprint.route('/tick')
class TickResource(BookingResourceBase):
    blueprint = BookingResourceBase.blueprint

    @blueprint.arguments(BookJsonSchema)
    def post(self):
        CarManager.tick()
