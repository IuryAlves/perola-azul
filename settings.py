# coding: utf-8

import os


DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', 27017)
DEBUG = os.getenv('DEBUG', True)
ENABLE_CORS = os.getenv('DEBUG', True)
SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:////tmp/test.db')
