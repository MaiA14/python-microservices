
from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
import requests

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=False, autoincrement=False)
    name = db.Column(db.String(200))
    image = db.Column(db.String(200))


class MovieUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'movie_id', name='user_movie_unique')


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ='mysql://root:root@db/main'

@app.route('/')
def index():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')