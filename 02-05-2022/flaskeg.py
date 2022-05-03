##import flask
##
##
##app = flask.Flask(__name__)
##app.config["DEBUG"] = True
##
##
##@app.route('/', methods = ['GET'])
##
##def home():
##    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant</p>"
##
##app.run()




# Another example
from flask import request, jsonify, Flask

app = Flask(__name__)
app.config["DEBUG"] = True

books = [
          {'id' : 0,
           'title' : 'A Fire Upon the Deep',
           'author' : 'Vernor Vinge',
           'first_sentence' : 'The coldsleep itself was dreamless.',
           'year_published' : '1992'},
          {'id' : 1,
           'title' : 'The Ones Who Walk Away From Omelas',
           'author' : 'Ursula K. Le Guin',
           'first_sentence' : 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas.',
           'year_published' : '1973'},
          {'id' : 2,
           'title' : 'Dhalgren',
           'author' : 'Samuel R. Delany',
           'first_sentence' : 'to wound the autumnal city.',
           'year_published' : '1975'},
        ]

@app.route('/', methods = ['GET'])
def home():
    return "hello to my api"


@app.route('/books/all', methods = ['GET'])
def api_all():
    return jsonify(books)

app.run()
