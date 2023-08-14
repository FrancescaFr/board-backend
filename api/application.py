from flask import Flask
# test heroku push
# added from project template:
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    # vercel test code
    # @app.route("/")
    # def home():
    #     return "Hello from Vercel"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URL")

    # Import models here for Alembic setup
    # from models.ExampleModel import ExampleModel

    from routes import hello_bp
    from routes import cards_bp
    from routes import boards_bp

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    # from .routes import example_bp
    # app.register_blueprint(example_bp)
    app.register_blueprint(hello_bp)
    app.register_blueprint(cards_bp)
    app.register_blueprint(boards_bp)

    # import models to make visible to app/db
    # from models.board import Board
    # from models.card import Card
    
    CORS(app)
    return app
