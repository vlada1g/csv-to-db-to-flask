from sqlalchemy import exc
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:!Vty1608995@db/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from api import routes,models