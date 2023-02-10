# Напишите вьюшку для запросов /search/?s=<s> которая бы выводила слова,
# в которых содержится указанная подстрока.
# Если ничего не нашлось – верните 404

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
@app.route('/search/')
def page_search():
    s = request.values.get("s")
    if s is None:
        return ""
    result = [word for word in list(alphabet.values()) if s in word.lower()]
    return ", ".join(result)

app = Flask(__name__)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)

