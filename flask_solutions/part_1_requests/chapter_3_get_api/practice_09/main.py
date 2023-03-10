from dataclasses import dataclass
from flask import Flask, request

app = Flask(__name__)

data = [
    ("π", "Apple Green", "fruit", 45),
    ("π", "Apple Red", "fruit", 49),
    ("π", "Banana", "fruit", 95),
    ("π₯", "Avocado", "fruit", 160),
    ("π", "Tomato", "veggie", 20),
    ("π₯¦", "Broccoli", "veggie", 34),
    ("π₯", "Carrot", "veggie", 100),
    ("πͺ", "Cookie", "sweets", 514),
    ("π©", "Donut", "sweets", 300),
    ("π°", "Cake", "sweets", 400),
]


def get_cats_from_products(products):
    return list(set([pro[2] for pro in products]))


@app.get("/")
def view_root():
    page = "<a href='/api/1/categories/'>ΠΡΠ΅ ΠΊΠ°ΡΠ΅Π³ΠΎΡΠΈΠΈ</a><br>"

    return page

@app.get('/api/1/categories/')
def func_name():
    return get_cats_from_products(data)

app.run()
