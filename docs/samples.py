from controller.products import (get_all_products, get_product_by_id, insert_product, delete_product, update_product)
from models.Product import Product


# print(get_all_products())

# print(get_product_by_id(2))

# print(insert_product('Twist & Shout 567g', 'Double filled chocolate cookies', 2000, 3, 3))

# print(delete_product(3))

# print(update_product(2, 'Café Nariño 500g', 'Soft coffee from Colombia', 15900, 2, 2))

# print(get_all_products())

product_from_db = get_product_by_id(2)

product = Product(product_from_db[1], product_from_db[2], product_from_db[3], product_from_db[4], product_from_db[5]).with_id(product_from_db[0])

print(product.id)
print(product.name)