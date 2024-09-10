from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuring the SQLAlchemy database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cars.db"

# Creating a SQLAlchemy database instance
db = SQLAlchemy(app)  # Bind SQLAlchemy to the Flask app


# Defining a SQLAlchemy model for the 'cars' table
class CarModel(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    color = db.Column(db.String(20), nullable=False)


# Creating all tables defined by SQLAlchemy models with context of app
with app.app_context():
    db.create_all()


# Handling HTTP GET requests for retrieving car data
@app.route("/", methods=["GET"])
def get_cars():
    cars = CarModel.query.all()
    return jsonify(
        [
            {
                "id": car.id,
                "brand": car.brand,
                "model": car.model,
                "price": car.price,
                "color": car.color,
            }
            for car in cars
        ]
    )


# Handling HTTP POST requests for adding new car data by maintaining schema
@app.route("/", methods=["POST"])
def create_car():
    data = request.get_json()  # Get the JSON data sent in the request
    brand = data.get("brand")
    model = data.get("model")
    price = data.get("price")
    color = data.get("color")

    if not all([brand, model, price, color]):
        return jsonify({"error": "Missing data"}), 400

    car = CarModel(brand=brand, model=model, price=price, color=color)
    db.session.add(car)
    db.session.commit()

    return (
        jsonify(
            {
                "id": car.id,
                "brand": car.brand,
                "model": car.model,
                "price": car.price,
                "color": car.color,
            }
        ),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True)
