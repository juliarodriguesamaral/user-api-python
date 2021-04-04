from flask import Flask, jsonify
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_object('config')

from .routes import routes