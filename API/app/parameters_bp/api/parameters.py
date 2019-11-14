from functools import wraps
from werkzeug.exceptions import Forbidden
from flask import request
from flask_restplus import Resource
from marshmallow import Schema, fields, validates, ValidationError
from sqlalchemy.exc import SQLAlchemyError

from app import db
from config import Config
from app.parameters_bp.models import Parameters
from app.parameters_bp import parameters_api
from app.parameters_bp.schemas import CreateParametersSchema



def authentication_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if not request.authorization:
            raise Forbidden

        if request.authorization['username'] == Config.AUTH_USERNAME and \
                request.authorization['password'] == Config.AUTH_PASSWORD:
            return f(*args, **kwargs)
        else:
            raise Forbidden
    return wrapped

@parameters_api.route('/', endpoint='parameters', methods = ['GET', 'POST'])
class ParametersAPI(Resource):
    # create_parameters_schema = CreateParametersSchema(many=False)
    @authentication_required
    def get(self):
        parametar = db.session.\
                query(Parameters).\
                order_by(Parameters.id.desc()).\
                first()
        return parametar.param1;
    def post(self):
        data = request.get_json(force=True)
        parameter = Parameters(param1 = data['param1'])
       # send_data();
        try:
            db.session.add(parameter)
            db.session.commit()
        except SQLAlchemyError as sqlalchemy_error:
            print(f"SqlAlchemy error:: {sqlalchemy_error}")
            return {'message': 'Database error.'}, 500
        except Exception as error:
            print(f"Unknown error:: {error}")
            return {'message': 'Unknown error.'}, 500
        return {'message': 'Parameters successfully created.'}, 200
