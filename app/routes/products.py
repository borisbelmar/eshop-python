from flask import Blueprint, jsonify, request, abort
from app.models import ProductSchema
from app.controller import get_product_by_id, get_all_products, insert_product, remove_product, update_product

products_blueprint = Blueprint('products_blueprint', __name__)

@products_blueprint.route('/', methods=['GET'])
def get_products():
    return jsonify(get_all_products())

@products_blueprint.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = get_product_by_id(id)
    if product is None:
        abort(404)
    return product

@products_blueprint.route('/', methods=['POST'])
def post_product():
    data = request.get_json()
    return insert_product(data)

@products_blueprint.route('/<int:id>', methods=['PUT'])
def put_product(id):
    product = get_product_by_id(id)
    if product is None:
        abort(404)
    data = request.get_json()
    product.update(data)
    return update_product(id, product)

@products_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    return remove_product(id)