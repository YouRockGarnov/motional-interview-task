from flask import (
    Flask,
    jsonify,
    json,
    make_response,
    request
)
from flask_smorest import Api
from app.booking.resources import blueprint as booking_blueprint


app = Flask(__name__)
app.config.from_object("config.Config")

api = Api(app)
api_prefix = '/api'
api.register_blueprint(booking_blueprint, url_prefix=api_prefix)


@app.errorhandler(Exception)
def handle_exception(error):
    return make_response(jsonify({'message': str(error)}), 500)

