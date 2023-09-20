from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = ('postgres://ocxkhvhn:uoQJ8uETZxmQCkxgzZx9l7vQLradKLlM@tai.db.elephantsql.com'
                                         '/ocxkhvhn')

db = SQLAlchemy(app)
