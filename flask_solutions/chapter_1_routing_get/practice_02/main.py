# Напишите вьюшку для запросов типа /find/?letter=<letter>,
# которая возвращает букву на основе квери-параметра.

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


@app.route('/find/')
def page_letter():

    letter = request.values.get("letter").upper()
    if not letter:
        return "Буква не передана"

    letter_name = alphabet.get(letter)
    if not letter_name:
        return "Нет такой буквы!"

    return letter_name


app.run(debug=True)


