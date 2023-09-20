from flask import jsonify, request
from werkzeug import exceptions
from application import app, db
from application.models import Character


@app.route("/")
def hello_world():
    return jsonify({
        "message": "Welcome",
        "description": "Characters API",
        "endpoints": [
            "GET /",
            "GET /characters",
            "GET /characters/id",
            "POST /characters"
        ]
    }), 200


@app.route("/characters")
def show_characters():
    try:
        characters = Character.query.all()
        data = [c.json for c in characters]
        return jsonify({"characters": data})
    except:
        raise exceptions.InternalServerError


@app.route("/characters", methods=["POST"])
def create_character():
    if request.method == "POST":
        try:
            print("🌕🌕🌕🌕", request.json)
            name, age, catch_phrase = request.json.values()
            new_character = Character(name=name, age=age, catch_phrase=catch_phrase)

            db.session.add(new_character)
            db.session.commit()

            return jsonify({"data": new_character.json}), 201
        except:
            print("❌❌❌", request)
            raise exceptions.BadRequest(f"We cannot process your request")


@app.route("/characters/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show_character(id):
    if request.method == "GET":
        try:
            character = Character.query.filter_by(id=id).first()
            return jsonify({"data": character.json}), 200
        except:
            raise exceptions.NotFound("you get it")

    if request.method == "PATCH":
        data = request.json
        character = Character.query.filter_by(id=id).first()

        for (attribute, value) in data.items():
            if hasattr(character, attribute):
                setattr(character, attribute, value)

        db.session.commit()

        return jsonify({"data": character.json})

    if request.method == "DELETE":
        character = Character.query.filter_by(id=id).first()
        db.session.delete(character)
        db.session.commit()
        return f"Character Deleted", 204


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"Oops {err}"}), 404


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": f"Oops {err}"}), 500


@app.errorhandler(exceptions.BadRequest)
def handler_400(err):
    return jsonify({"error": f"Oops {err}"}), 400


