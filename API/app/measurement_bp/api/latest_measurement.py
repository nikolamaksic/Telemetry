from flask_restplus import Resource
from sqlalchemy.orm.exc import NoResultFound

from app import db
from app.measurement_bp.models import Measurement
from app.measurement_bp import measurement_api
from app.measurement_bp.schemas import GetMeasurementSchema


@measurement_api.route('/latest')
class LatestMeasurementAPI(Resource):

    latest_measurement_schema = GetMeasurementSchema()

    def get(self):
        """
        HTTP method GET is used for retrieving the
        """
        try:
            measurement = db.session.\
                query(Measurement).\
                order_by(Measurement.id.desc()).\
                first()
        except NoResultFound as no_result_found_error:
            print(f"SqlAlchemy error:: {no_result_found_error}")
            return {'message': 'No results found.'}, 404
        except Exception as error:
            print(f"Unknown error:: {error}")
            return {'message': 'Unknown error.'}, 500

        return self.latest_measurement_schema.dump(measurement), 200
