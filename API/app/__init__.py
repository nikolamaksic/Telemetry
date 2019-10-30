from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
db = SQLAlchemy()
migrate = Migrate()



def create_app(config):
    """ The Application Factory function that instantiates an app singleton
        and attaches the configuration from config object and returns it """
    app = Flask(__name__)
    app.config.from_object('config.development.Development')
    db.init_app(app)
    
    migrate.init_app(app, db)
    from app.measurement_bp import measurement_blueprint
    #from app.test_bp import test_blueprint
    #app.register_blueprint(test_blueprint)
    app.register_blueprint(measurement_blueprint)
    return app
