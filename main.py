from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.customer.customer_routes import customer_bp
from controllers.restaurant.restaurant_routes import restaurant_bp
from controllers.restaurant.items_routes import items_bp
from db.database import init_db
app = Flask(__name__)


app.register_blueprint(customer_bp)
app.register_blueprint(restaurant_bp)
app.register_blueprint(items_bp, url_prefix='/restaurants')

init_db()
app.run(debug=True)
