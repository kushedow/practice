from dataclasses import dataclass
from flask import Flask, request

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
    ("🍎", "Apple Red", "fruit", 49),
    ("🍌", "Banana", "fruit", 95),
    ("🥑", "Avocado", "fruit", 160),
    ("🍅", "Tomato", "veggie", 20),
    ("🥦", "Broccoli", "veggie", 34),
    ("🥕", "Carrot", "veggie", 100),
    ("🍪", "Cookie", "sweets", 514),
    ("🍩", "Donut", "sweets", 300),
    ("🍰", "Cake", "sweets", 400),
]

products = [Product(*el) for el in data]


def get_product_by_kcal(products, from_val=0.0, to_val=float("inf")):
    """ Возвращает продукты с калорийностью в указанном интервале """
    return [pro for pro in products if from_val <= pro.kcal <= to_val]


@app.get("/")
def view_root():
    page = "<a href='/api/1/products/?kcal_to=100'>До 100</a><br>" \
           "<a href='/api/1/products/?kcal_from=100&kcal_to=200'>От 100 до 200</a><br>" \
           "<a href='/api/1/products/?cat=kcal_from'>От 300</a><br>" \
           "<a href='/api/1/products/'>Все сразу</a><br>"

    return page


@app.get('/api/1/products/')
def view_category_page():

    # получаем ограничения интервала
    from_val = float(request.values.get('kcal_from', 0))
    to_val = float(request.values.get('kcal_to', float("inf")))

    # возвращаем с фильтром
    return get_product_by_kcal(products, from_val, to_val)


app.run()
