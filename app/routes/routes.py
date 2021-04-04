from app import app
from flask import jsonify


@app.route('/', methods=['GET'])
def root():
      return jsonify({'message': 'Olá mundo com python!'})