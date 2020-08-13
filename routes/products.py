from flask import Blueprint, jsonify, request
from models.ProductSchema import ProductSchema
from controller.products import get_product_by_id, get_all_products, insert_product, delete_product, update_product

products_blueprint = Blueprint('products_blueprint', __name__)

@products_blueprint.route('/', methods=['GET'])
def get_products():
    return jsonify(get_all_products())

@products_blueprint.route('/<int:id>', methods=['GET'])
def get_product(id):
    return get_product_by_id(id)

@products_blueprint.route('/', methods=['POST'])
def post_product():
    data = request.get_json()
    product = ProductSchema()
    return product.dump(data)