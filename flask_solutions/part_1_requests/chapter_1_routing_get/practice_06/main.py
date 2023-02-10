# Напишите вьюшку для запросов /get-some/?limit=<limit>&offset=<offset>,
# которая возвращает указанное количества с указанной позиции.
# Если с таким отступом ничего нет или лимит нулевой – возвращает “-”.

from flask import Flask, request

alphabet = {
  "A": "Alfa",
  "B": "Bravo",
  "C": "Charlie",
  "D": "Delta",
  "E": "Echo",
  "F": "Foxtrot",
  "G": "Golf",
  "H": "Hotel",
  "I": "India",
  "J": "Juliett",
  "K": "Kilo",
  "L": "Lima",
  "M": "Mike",
  "N": "November",
  "O": "Oscar",
  "P": "Papa",
  "Q": "Quebec",
  "R": "Romeo",
  "S": "Sierra",
  "T": "Tango",
  "U": "Uniform",
  "V": "Victor",
  "W": "Whiskey",
  "X": "X-ray",
  "Y": "Yankee",
  "Z": "Zulu",
}

app = Flask(__name__)


@app.route('/letters/')
def page_display_letters():

    limit = request.values.get("limit")
    offset = request.values.get("offset")

    if (not limit) or (not offset):
        return "-"

    limit = int(limit)
    offset = int(offset)

    sliced_letters = list(alphabet.keys())[offset:offset+limit]

    if not sliced_letters:
        return "-"

    return "".join(sliced_letters)


app.run(debug=True)


