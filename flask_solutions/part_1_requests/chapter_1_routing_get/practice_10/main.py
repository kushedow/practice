import string

from flask import Flask, request

app = Flask(__name__)

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
alphabet_keys = list(alphabet.keys())


@app.route('/letters/')
def limit_offset_sort():
    offset,limit,sort = request.args.get('offset')
    limit = request.args.get('limit')
    sort = request.args.get('sort')

    letters = alphabet_keys.copy()

    if offset is not None:
        letters = letters[int(offset):]

    if limit is not None:
        letters = letters[:int(limit)]

    if sort == "asc":
        letters.sort()

    elif sort == "desc":
        letters.sort(reverse=True)

    return "".join(letters)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
