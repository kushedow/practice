# Напишите вьюшку для запросов /between/?from=<letter>&to=<letter> ,
# которая возвращает буквы в промежутке между указанными в любом направлении или прочерк,
# если между указанными буквами ничего нет.

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


@app.route('/between/')
def page_between():

    letter_from = request.values.get("from").upper()
    letter_to = request.values.get("to").upper()

    if (not letter_from) or (not letter_to):
        return "-"

    list_of_letters = list(alphabet.keys())

    try:
        start_position = list_of_letters.index(letter_from)
        end_position = list_of_letters.index(letter_to)
    except ValueError:
        return "-"

    letters = list_of_letters[start_position+1:end_position]

    if len(letters) == 0:
        return "-"

    return "".join(letters).lower()


app.run(debug=True)

