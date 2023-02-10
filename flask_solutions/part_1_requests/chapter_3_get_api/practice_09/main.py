from dataclasses import dataclass
from flask import Flask, request

app = Flask(__name__)

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


def get_cats_from_products(products):
    return list(set([pro[2] for pro in products]))


@app.get("/")
def view_root():
    page = "<a href='/api/1/categories/'>Все категории</a><br>"

    return page

@app.get('/api/1/categories/')
def func_name():
    return get_cats_from_products(data)

app.run()
