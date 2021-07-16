from flask import (
    Flask,
    jsonify,
    json,
    make_response,
    request
)
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_babel import Babel
from flask_mail import Mail
from flask_apscheduler import APScheduler
from flask_talisman import Talisman

app = Flask(__name__)
app.register_blueprint(resources.blueprint)


CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

app.config.from_object("config.Config")


@app.errorhandler(Exception)
def handle_exception(error):
    logger.error(str(type(error).__name__), show_exc_info=True)
    return make_response(jsonify({'message': str(error)}), 500)

