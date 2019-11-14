from functools import wraps
from werkzeug.exceptions import Forbidden
from flask import request
from flask_restplus import Resource
from marshmallow import Schema, fields, validates, ValidationError
from sqlalchemy.exc import SQLAlchemyError

from app import db
from config import Config



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

@app.route('/<status>', method =  'POST')

@authentication_required
def change_status(status):
    if(status==0):
        return{'message': 'Status scuccesful.'}, 200
