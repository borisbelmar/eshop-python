from flask import Blueprint, request, abort
from app.models import ProductSchema
from app.controller import customer_register, customer_login, customer_info
from app.middlewares import is_auth

customers_blueprint = Blueprint('customers_blueprint', __name__)

@customers_blueprint.route('/register', methods=['POST'])
def customer_insert():
    customer = request.get_json()
    return customer_register(customer)

@customers_blueprint.route('/login', methods=['POST'])
def customer_login_route():
    body = request.get_json()
    if body is None or body.get('email') is None or body.get('password') is None:
        abort(400, 'MISSING_EMAIL_OR_PASSWORD')
    return customer_login(body['email'], body['password'])

@customers_blueprint.route('/account', methods=['GET'])
@is_auth
def get_customer_info(token_payload):
    return customer_info(token_payload['sub'])
