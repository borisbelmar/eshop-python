from flask import Flask, jsonify
from controller.products import get_product_by_id, get_all_products

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello_world():
    return 'Holi'

@app.route('/products')
def get_products():
    return jsonify(get_all_products())

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = get_product_by_id(id)
    product_dict = {
        'id': product[0],
        'name': product[1] 
    }
    return jsonify(product_dict)