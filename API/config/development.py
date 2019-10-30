from config import Config


class Development(Config):
    """ The class whose fields act as configuration development environment
        constants """
    ENV_TYPE = "Development"

    DB_NAME = "etfrobotics_2019"
    DB_USER = "ETFRoboticsUser"
    DB_PASSWD = "fastandfourier"
    DB_HOST = "127.0.0.1"
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.\
        format(DB_USER, DB_PASSWD, DB_HOST, DB_PORT, DB_NAME)
# maintenance database 'postgres'
# server name 'ETFRoboticsUser'