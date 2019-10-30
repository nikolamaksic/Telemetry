import os
from config import Config


class Production(Config):
    """ The class whose fields act as configuration production environment
        constants """
    ENV_TYPE = "Production"

    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
