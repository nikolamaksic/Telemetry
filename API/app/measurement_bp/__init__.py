from flask import Blueprint
from flask_restplus import Api

APP_NAME = 'measurement'
measurement_blueprint = Blueprint(APP_NAME,
                                  __name__,
                                  url_prefix='/{}'.format(APP_NAME))


measurement_api = Api(measurement_blueprint)

import app.measurement_bp.api
