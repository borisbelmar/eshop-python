from flask import Blueprint, jsonify, request
from app.models import BrandSchema
from app.controller import get_brand_by_id, get_all_brands, insert_brand, delete_brand, update_brand

brands_blueprint = Blueprint('brands_blueprint', __name__)

@brands_blueprint.route('/', methods=['GET'])
def get_brands():
    return jsonify(get_all_brands())

@brands_blueprint.route('/<int:id>', methods=['GET'])
def get_brand(id):
    return get_brand_by_id(id)

@brands_blueprint.route('/', methods=['POST'])
def post_brand():
    data = request.get_json()
    brand = BrandSchema()
    return brand.dump(data)