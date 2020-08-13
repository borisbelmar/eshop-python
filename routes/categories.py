from flask import Blueprint, jsonify, request
from models.CategorySchema import CategorySchema
from controller.categories import get_category_by_id, get_all_categories, insert_category, delete_category, update_category

categories_blueprint = Blueprint('categories_blueprint', __name__)

@categories_blueprint.route('/', methods=['GET'])
def get_categories():
    return jsonify(get_all_categories())

@categories_blueprint.route('/<int:id>', methods=['GET'])
def get_category(id):
    return get_category_by_id(id)

@categories_blueprint.route('/', methods=['POST'])
def post_category():
    data = request.get_json()
    category = CategorySchema()
    return category.dump(data)