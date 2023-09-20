from application import db


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    age = db.Column(db.Integer, nullable=False)
    catch_phrase = db.Column(db.String(100), nullable=False)


