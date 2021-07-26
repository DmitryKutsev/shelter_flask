

DEBUG = True
LOG_LEVEL = 'DEBUG'  # CRITICAL / ERROR / WARNING / INFO / DEBUG

SERVER_NAME = '127.0.0.1:8000'
SECRET_KEY = 'value_from_os_env_variables'

# SQLAlchemy.
db_uri = 'postgresql://postgres:postgres@postgres:5432'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
