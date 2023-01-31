# Напишите вьюшку для запросов /get-some/<number>,
# которая возвращает указанное количество букв
# или - если передан 0

from flask import Flask

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


@app.route('/getsome/<int:number>/')
def page_display_letters(number):

    letters = list(alphabet.keys())
    sliced_letters = letters[:number]
    return "".join(sliced_letters)


app.run(debug=True)

