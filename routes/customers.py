from flask import Blueprint, request, abort
from models import ProductSchema
from controller.customers import customer_register, customer_login, customer_info
from middlewares import is_auth

customers_blueprint = Blueprint('customers_blueprint', __name__)

@customers_blueprint.route('/register', methods=['POST'])
def customer_insert():
    customer = request.get_json()
    return customer_register(customer)

@customers_blueprint.route('/login', methods=['POST'])
def customer_login_route():
    body = request.get_json()
    if body is None or body['email'] is None or body['password'] is None:
        abort(400)
    return customer_login(body['email'], body['password'])

@customers_blueprint.route('/account', methods=['GET'])
@is_auth
def get_customer_info(token_payload):
    return customer_info(token_payload['sub'])
