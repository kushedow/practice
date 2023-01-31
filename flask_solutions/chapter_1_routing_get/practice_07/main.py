# Напишите вьюшку для запросов /letters/page/<page_number>,
# которая выводила бы по пять элементов, причем, если страница не указана,
# выводятся первые 5 элементов, если же для указанной страницы не хватает элементов,
# возвращается статус-код 404.


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
letters = list(alphabet.keys())

app = Flask(__name__)


@app.route('/letters/')
@app.route('/letters/page/<int:page>/')
def page_display_letters(page: int = 1):

    per_page = 5
    sliced_letters = letters[per_page*(page-1):per_page*page]\

    if len(sliced_letters) < per_page:
        return " ", 404

    return "".join(sliced_letters)


app.run(debug=True, port=5002)
