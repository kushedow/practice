import random

from flask import Flask, request

app = Flask(__name__)

data = ["milk", "sugar", "cookies", "corn-flakes", "nutella"]


@app.get("/")
def view_root():
    return "<a href='/api/1/grocery/'></a>"


@app.get('/api/1/grocery/')
def view_grocery():
    return data


app.run()
