class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['price'])

if __name__ == '__main__':
    product_data = {'name': 'Laptop', 'price': 200}
    product = Product.from_dict(product_data)
    print(f'Product name: {product.name}, Price: {product.price}')

