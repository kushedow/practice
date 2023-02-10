from dataclasses import dataclass
from flask import Flask

app = Flask(__name__)

@dataclass
class Product:
    pk: int
    icon: str
    name: str
    cat: str
    kcal: int

    def dict(self):
        return {
            "pk": self.pk,
            "icon": self.icon,
            "name": self.name,
            "cat": self.cat,
            "kcal": self.kcal,
        }

data = [
    ("1", "🍏", "Apple Green", "fruit", 45),
    ("2", "🍎", "Apple Red", "fruit", 49),
    ("3", "🍌", "Banana", "fruit", 95),
    ("4", "🥑", "Avocado", "fruit", 160),
    ("5", "🍅", "Tomato", "veggie", 20),
    ("6", "🥦", "Broccoli", "veggie", 34),
    ("7", "🥕", "Carrot", "veggie", 100),
    ("8", "🍪", "Cookie", "sweets", 514),
    ("9", "🍩", "Donut", "sweets", 300),
    ("10", "🍰", "Cake", "sweets", 400),
]

products = [Product(*el) for el in data]


def get_products_by_pks(products: list[Product], pks: list[int]):
    return [pro for pro in products if pro.pk in pks]


@app.get("/")
def view_root():
    page = "<a href='/api/1/products/1_2_3/'>Пример списка</a><br>"
    return page

@app.get('/api/1/products/<pks_raw>/')
def view_show_products(pks_raw):

    pks = pks_raw.split("_")
    return get_products_by_pks(products, pks)


app.run()
