#
# from app.booking.schemas.BookJsonSchema import BookJsonSchema
# from app.booking.schemas.BookResponseSchema import BookResponseSchema
# from app.managers.car_manager import CarManager
# from flask_smorest import Blueprint
# from flask.views import MethodView
#
#
# blueprint = Blueprint('Bookings', 'Bookings')
#
#
# @blueprint.route('/book')
# class BookResource(MethodView):
#     blueprint = BookingResourceBase.blueprint
#
#     @blueprint.arguments(BookJsonSchema)
#     def post(self, json_body):
#         result = CarManager.book_nearest_available_car(source=json_body['source'], destination=json_body['destination'])
#         return BookResponseSchema.load(result)
#
#
# @blueprint.route('/tick')
# class TickResource(MethodView):
#     blueprint = BookingResourceBase.blueprint
#
#     @blueprint.arguments(BookJsonSchema)
#     def post(self):
#         CarManager.tick()