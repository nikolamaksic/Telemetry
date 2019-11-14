from functools import wraps
from werkzeug.exceptions import Forbidden
from flask import request
from flask_restplus import Resource
from marshmallow import Schema, fields, validates, ValidationError
from sqlalchemy.exc import SQLAlchemyError

from app import db
from config import Config
from app.measurement_bp.models import Measurement
from app.measurement_bp import measurement_api
from app.measurement_bp.schemas import CreateMeasurementSchema


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


@measurement_api.route('/', endpoint='measurement')
class MeasurementAPI(Resource):
    """
    Endpoint class (API controller class) for measurement resource
    """
    create_measurement_schema = CreateMeasurementSchema(many=False)

    @authentication_required
    def post(self):
        """
        We are (naively) assuming that our data is fine
        """
        measurement_data = request.get_json(force=True)

        try:
            validated_measurement_data = \
                self.create_measurement_schema.load(measurement_data)
        except ValidationError as validation_error:
            print(f"Validation error:: {validation_error}")
            return {'message': 'Data validation error.'}, 400
        except Exception as error:
            print(f"Unknown error:: {error}")
            return {'message': 'Unknown error.'}, 500

        measurement = Measurement(
            front_left_weel=validated_measurement_data['front_left_weel'],
            front_right_weel=validated_measurement_data['front_right_weel'],
            back_left_weel=validated_measurement_data['back_left_weel'],
            back_right_weel=validated_measurement_data['back_right_weel'],
            servo_angle=validated_measurement_data['servo_angle']
        )

        try:
            db.session.add(measurement)
            db.session.commit()
        except SQLAlchemyError as sqlalchemy_error:
            print(f"SqlAlchemy error:: {sqlalchemy_error}")
            return {'message': 'Database error.'}, 500
        except Exception as error:
            print(f"Unknown error:: {error}")
            return {'message': 'Unknown error.'}, 500

        return {'message': 'Measurement successfully created.'}, 200


class GetMeasurementSchema(Schema):
    """
    Schema class used for serializing data pulled from DB for our
    GET endpoint
    """
    id = fields.Int(required=True)
    front_left_weel = fields.Float(required=True)
    front_right_weel = fields.Float(required=True)
    back_left_weel = fields.Float(required=True)
    back_right_weel = fields.Float(required=True)
    servo_angle = fields.Float(required=True)
    timestamp = fields.DateTime(required=True)
