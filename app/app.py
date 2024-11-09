import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config_app import get_logger
from sqlalchemy.orm import DeclarativeBase

logger = get_logger()


load_dotenv()


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
print(os.getenv("FLASK_DATABASE_PROD"))

def create_app(database=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = database or os.getenv("FLASK_DATABASE_PROD")    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("APP_TESTING") == "true"
    app.config["TESTING"] =  os.getenv("APP_TESTING") == "true"

    db.init_app(app)

    with app.app_context():
        db.create_all()
    from app.routes import register_routes

    register_routes(app, db)

    migrate = Migrate(app, db)
    logger.info(migrate)

    return app


if __name__ == "__main__":
    create_app().run(debug=True, port=10000)
