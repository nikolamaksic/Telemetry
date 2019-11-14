from flask import Blueprint
from flask_restplus import Api

APP_NAME = 'parameters'
parameters_blueprint = Blueprint(APP_NAME,
                                  __name__,
                                  url_prefix='/{}'.format(APP_NAME))


parameters_api = Api(parameters_blueprint)

import app.parameters_bp.api
