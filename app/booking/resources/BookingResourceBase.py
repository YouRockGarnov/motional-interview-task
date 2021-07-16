from flask import jsonify, make_response
from flask.views import MethodView
from flask_smorest import abort
from flask_smorest import Blueprint


class BookingResourceBase(MethodView):
    blueprint = Blueprint('Bookings', 'Bookings')

