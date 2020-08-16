from flask import Blueprint, request, abort
from models import ProductSchema
from controller.customers import customer_register

customers_blueprint = Blueprint('customers_blueprint', __name__)

@customers_blueprint.route('/', methods=['POST'])
def customer_insert():
    customer = request.get_json()
    return customer_register(customer)