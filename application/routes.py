from flask import jsonify
from application import app
from application.models import Character


@app.route("/")
def hello_world():
    return jsonify({
        "message": "Welcome",
        "description": "Characters API",
        "endpoints": [
            "GET /",
            "GET /characters"
        ]
    }), 200


@app.route("/characters")
def show_characters():
    characters = Character.query.all()
    data = [c.json for c in characters]
    return jsonify({"characters": data})


@app.route("/characters/<id>")
def show_character(id):
    character = Character.query.filter_by(id=id).first()

    return jsonify({"data": character.json}), 200
