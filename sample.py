from flask import Flask, jsonify 

app=Flask(__name__)

@app.route('/')
def homepage():
    return 'Welcome to my Python Page!'

airlines = [
    {
        "id": 1,
        "name": "United"
    },
    {
        "id": 2,
        "name": "Frontier"
    },
    {
        "id": 3,
        "name": "Spirit"
    }
]

@app.route('/airlines')
def arilines():
    return jsonify(airlines)

@app.route('/airlines/<id>')
def airline(id):
    for airline in airlines:
        if airline['id'] == int(id):
            return jsonify(airline)

            