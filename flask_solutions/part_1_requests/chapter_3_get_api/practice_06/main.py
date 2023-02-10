from dataclasses import dataclass
from flask import Flask, abort

app = Flask(__name__)


@dataclass
class Product:
    icon: str
    name: str
    cat: str
    kcal: int

    def dict(self):

        return {
            "icon": self.icon,
            "name": self.name,
            "cat": self.cat,
            "kcal": self.kcal,
        }


data = [
    ("🍏", "Apple Green", "fruit", 45),
    ("🍎", "Apple Red", "fruit", 45),
    ("🍌", "Banana", "fruit", 45),
    ("🥑", "Avocado", "fruit", 45),
    ("🍅", "Tomato", "veggie", 45),
    ("🥦", "Broccoli", "veggie", 45),
    ("🥕", "Carrot", "veggie", 45),
    ("🍪", "Cookie", "sweets", 45),
    ("🍩", "Donut", "sweets", 45),
    ("🍰", "Cake", "sweets", 45),
]
products = [Product(*el) for el in data]


def get_product_by_name(products, name):
    """ Возврашает продукт по имени если такой есть"""
    for product in products:
        if product.name.lower() == name.lower():
            return product

@app.get("/")
def view_root():
    return "<a href='/api/1/products/cookies/'>Перейти</a>"


@app.get('/api/1/products/<product_name>/')
def view_product_by_name(product_name):

    product = get_product_by_name(products, product_name)

    return product.dict() if product else abort(404)

app.run()
