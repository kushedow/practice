# Напишите вьюшку для запросов  /check/<letter>/<word>
# для проверки соответствия буквы ее расшифровке:

from flask import Flask, render_template

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


@app.route('/check/<letter_short>/<letter_full>/')
def page_check_letter(letter_short: str, letter_full: str):

    if letter_short not in alphabet:
        return "False"

    if alphabet[letter_short] != letter_full:
        return "False"
        
    return "True"



app.run(debug=True)

