from application import db
from application.models import Character

db.drop_all()
print("Dropping database")
db.create_all()
print("Creating database")

print("Seeding database")
entry1 = Character(name="Phoebe", age=29, catch_phrase="My eyes, my eyes")

entry2 = Character(name="Urkel", age=12, catch_phrase="Did I do that?")

entry3 = Character(name="Edward Elric (FMA)", age=22, catch_phrase="Who are you calling short?")

db.session.add(entry1)
db.session.add_all([entry2, entry3])

db.session.commit()
