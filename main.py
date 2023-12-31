from flask import Flask
from controllers.customer.customer_routes import customer_bp
from controllers.restaurant.restaurant_routes import restaurant_bp
from controllers.restaurant.items_routes import items_bp
from controllers.auth.auth_routes import auth_bp
from controllers.order.order_routes import order_bp
from controllers.restaurant.cupom_routes import cupom_bp
from controllers.search.search_routes import search_bp
from controllers.customer.avaliacao_routes import avaliacao_bp
from controllers.customer.favorite_routes import favorite_bp
from via_cep.via_cep_routes import via_cep_bp
from db.database import init_db
from flask_jwt_extended import jwt_required
from utils.data_base_util import populate_category_table, populate_restriction_table
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')

app.register_blueprint(customer_bp)
app.register_blueprint(restaurant_bp)
app.register_blueprint(items_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(order_bp)
app.register_blueprint(cupom_bp)
app.register_blueprint(search_bp)
app.register_blueprint(avaliacao_bp)
app.register_blueprint(favorite_bp)
app.register_blueprint(via_cep_bp)
#populate_restriction_table()
# populate_category_table()
init_db()



app.run(host='0.0.0.0', port=5000, debug=True)
