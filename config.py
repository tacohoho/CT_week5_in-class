import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "You will never guess..."
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:9248jong@localhost:5432/operators_drones'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URI')