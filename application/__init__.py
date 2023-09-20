from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.json_provider_class.sort_keys = False
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql://ocxkhvhn:uoQJ8uETZxmQCkxgzZx9l7vQLradKLlM@tai.db.elephantsql.com'
                                         '/ocxkhvhn')

db = SQLAlchemy(app)
