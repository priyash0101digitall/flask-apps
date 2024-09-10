# Importing the Flask module
from flask import Flask

# Importing SQLAlchemy for database operations
from flask_sqlalchemy import SQLAlchemy

# Importing Marshmallow for data serialization and validation
from marshmallow import Schema, fields

# Importing Blueprint and Api for building RESTful APIs
from flask_smorest import Blueprint, Api

# Importing MethodView for defining views with explicit HTTP methods
from flask.views import MethodView

# Creating a Flask app instance
app = Flask(__name__)

# Configuring the SQLAlchemy database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cars.db"

# Configuring the API title, version, and OpenAPI settings
app.config["API_TITLE"] = "cars_api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.0"
app.config["OPENAPI_URL_PREFIX"] = "/"

# Configuring the Swagger UI path and URL
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# Creating a SQLAlchemy database instance
db = SQLAlchemy()

# Defining a SQLAlchemy model for the 'cars' table
class CarModel(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    color = db.Column(db.String(20), nullable=False)

# binding SQLAlchemy object with the Flask app
db.init_app(app)

# Creating all tables defined by SQLAlchemy models with context of app
with app.app_context():
    db.create_all()

# Defining a Marshmallow schema for validating and serializing car data
class CarSchema(Schema):
    id = fields.Integer(dump_only=True)
    brand = fields.String(required=True)
    model = fields.String(required=True)
    price = fields.Float(required=True)
    color = fields.String(required=True)

# Creating a Blueprint for the car API endpoints
cars_bp = Blueprint("cars_bp_name", __name__, url_prefix="/cars")

# Defining a resource class for handling car API endpoints
@cars_bp.route("/")
class CarsResource(MethodView):
    # Handling HTTP GET requests for retrieving car data
    @cars_bp.response(200, CarSchema(many=True))
    def get(self):
        return CarModel.query.all()

    # Handling HTTP POST requests for adding new car data by maintaining schema
    @cars_bp.arguments(CarSchema)
    @cars_bp.response(201, CarSchema)
    def post(self, new_car):
        car = CarModel(**new_car)
        db.session.add(car)
        db.session.commit()
        return car

# Creating an Api instance and registering the Blueprint with it
car_api = Api(app)
car_api.register_blueprint(cars_bp)