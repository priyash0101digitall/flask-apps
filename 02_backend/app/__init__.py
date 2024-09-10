from flask import Flask
from db import db
from flask_smorest import Api
from app.blueprints import phones_blp
from flask_migrate import Migrate
from config import Config

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)
    
    migrate = Migrate(app, db)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
    api = Api(app)

    # register blueprints
    api.register_blueprint(phones_blp)

    return app