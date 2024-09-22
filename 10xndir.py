class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"

class Store:
    def __init__(self):
        self.products = {}

    def __iadd__(self, product):
        if isinstance(product, Product):
            if product.name in self.products:
                self.products[product.name]['Qanak'] += 1
            else:
                self.products[product.name] = {'product': product, 'Qanak': 1}
        return self

    def __isub__(self, product_name):
        if product_name in self.products:
            if self.products[product_name]['Qanak'] > 1:
                self.products[product_name]['Qanak'] -= 1
            else:
                del self.products[product_name]
        return self

    def __repr__(self):
        return '\n'.join(
            f"{product['product'].name}: {product['Qanak']} (Price: {product['product'].price})"
            for product in self.products.values()
        )

store = Store()

store += Product("Apple", 0.5)
store += Product("Banana", 0.3)
store += Product("Apple", 0.5)

print("Xanuti apranqy, stacumic heto")
print(store)

store -= "Apple"

print("\nXanuti apranqy, caxveluc heto")
print(store)

#store -= "Banana"
store -= "Apple"

print("\nXanuti apranqy, amboxjy vachareluc heto")
print(store)
