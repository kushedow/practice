from flask import Flask, render_template

app = Flask(__name__)

data = [
    {"name": "milk", "unit_price": 50, "amount": 3, "total": 150, "cat": "mil"},
    {"name": "sugar", "unit_price": 30, "amount": 3, "total": 90},
    {"name": "cookies", "unit_price": 50, "amount": 4, "total": 200},
    {"name": "corn-flakes", "unit_price": 70, "amount": 2, "total": 140},
    {"name": "nutella", "unit_price": 125, "amount": 1, "total": 250},
]


def filter_by_product_name(products, product_name):
    """Функция для фильтрации продуктов по имени"""
    return [pro for pro in products if pro["name"] == product_name]


@app.get("/")
def view_root():
    return "<a href='/api/1/expanses/cookies/'>Перейти</a>"


@app.get('/api/1/expanses/<product>/')
def view_expanses_by_product(product):
    # Фильтруем продукты
    filtered_products = filter_by_product_name(data, product)
    # Возвращаем результат
    return filtered_products


if __name__ == '__main__':
    app.run()
