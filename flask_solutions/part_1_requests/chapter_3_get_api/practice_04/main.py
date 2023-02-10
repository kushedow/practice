import random

from flask import Flask, request

app = Flask(__name__)

expenses = {
    "milk": 150,
    "sugar": 90,
    "cookies": 200,
    "corn-flakes": 140,
    "nutella": 250,
}


@app.get("/")
def view_root():
    return "<a href='/api/1/grocery-stats'>Перейтии</a>"


@app.get('/api/1/grocery-stats/')
def view_grocery_stats():
    grocery_prices = list(expenses.values())
    count = len(grocery_prices)
    total = sum(grocery_prices)
    max_value = max(grocery_prices)
    max_value = max(grocery_prices)
    avg = total / count

    return {
        "count": count,
        "total": total,
        "max": max_value,
        "min": max_value,
        "avg": avg,
    }

app.run()
