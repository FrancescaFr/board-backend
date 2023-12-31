import os

FLASK_APP = os.environ["FLASK_APP"]
FLASK_ENV = os.environ["FLASK_ENV"]
SECRET_KEY = os.environ["SECRET_KEY"]
SQLALCHEMY_DATABASE_URL=os.environ["SQLALCHEMY_DATABASE_URL"]
SQLALCHEMY_DATABASE_PRISMA_URL=os.environ["SQLALCHEMY_DATABASE_PRISMA_URL"]
SQLALCHEMY_DATABASE_URL_NON_POOLING=os.environ["SQLALCHEMY_DATABASE_URL_NON_POOLING"]
SQLALCHEMY_DATABASE_USER=os.environ["SQLALCHEMY_DATABASE_USER"]
SQLALCHEMY_DATABASE_HOST=os.environ["SQLALCHEMY_DATABASE_HOST"]
SQLALCHEMY_DATABASE_PASSWORD=os.environ["SQLALCHEMY_DATABASE_PASSWORD"]
SQLALCHEMY_DATABASE_DATABASE=os.environ["SQLALCHEMY_DATABASE_DATABASE"]


