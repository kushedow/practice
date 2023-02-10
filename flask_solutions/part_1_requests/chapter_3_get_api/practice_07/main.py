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


def get_product_by_cat(products, cat_name):

    return [pro for pro in products if pro.cat == cat_name]

@app.get("/")
def view_root():

    page = "<a href='/api/1/products/?cat=fruit'>Фрукты</a><br>" \
           "<a href='/api/1/products/?cat=veggie'>Овощи</a><br>" \
           "<a href='/api/1/products/?cat=sweets'>Сладкое</a><br>" \
           "<a href='/api/1/products/'>Все сразу</a><br>"

    return page


@app.get('/api/1/products/')
def view_category_page():

    # получаем название категории
    cat_name = request.values.get('cat')

    # если не получили – вернем не фильтруя
    if cat_name is None:
        return products

    # иначе вернем с фильтром
    return get_product_by_cat(products, cat_name)

app.run()
