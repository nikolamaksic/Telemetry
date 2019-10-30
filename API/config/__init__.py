class Config:
    """ The class whose fields act as configuration constants """
    ENV_TYPE = None

    DEBUG = True
    FLASK_HOST = '127.0.0.1'
    FLASK_PORT = 8000

    DB_NAME = None
    DB_USER = None
    DB_PASSWD = None
    DB_HOST = None
    DB_PORT = None

    AUTH_USERNAME = 's'
    AUTH_PASSWORD = 'd'

    SQLALCHEMY_TRACK_MODIFICATIONS = True