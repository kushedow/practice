import random

from flask import Flask

app = Flask(__name__)


@app.get("/")
def view_root():
    return "<a href='/api/1/random/'>Перейти</a>"


@app.get('/api/1/random/')
def view_random():
    value = random.randint(1, 10)
    return {"number": value}


app.run()
