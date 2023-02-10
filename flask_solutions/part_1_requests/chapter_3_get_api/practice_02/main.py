import random

from flask import Flask, request

app = Flask(__name__)


@app.get("/")
def view_root():
    return "<a href='/api/1/random/?from=5&to=10'>Перейти</a>" \
           "<a href='/api/1/random/?from=5'>Перейти</a>" \
           "<a href='/api/1/random/?to=5'>Перейти</a>"


@app.get('/api/1/random/')
def view_random():

    from_val = int(request.args.get("from", 1))
    to_val = int(request.args.get("to", 100))

    value = random.randint(from_val, to_val)
    return {"number": value}


app.run()
