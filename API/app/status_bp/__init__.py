from flask import Blueprint
from flask_restplus import Api

APP_NAME = 'status'
status_blueprint = Blueprint(APP_NAME,
                                  __name__,
                                  url_prefix='/{}'.format(APP_NAME))


status_api = Api(status_blueprint)


