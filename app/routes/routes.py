from app import app
from flask import jsonify

from app.views import users


@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'Olá mundo com python!'})


@app.route('/users', methods=['POST'])
def post_user():
    return users.post_user()
