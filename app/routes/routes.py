from app import app
from flask import jsonify

from app.views import users


@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'Olá mundo com python!'})


@app.route('/users', methods=['POST'])
def post_user():
    return users.post_user()


@app.route('/users/<id>', methods=['PUT'])
def put_user(id):
    return users.update_user(id)


@app.route('/users', methods=['GET'])
def get_users():
    return users.get_users()


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    return users.get_users(id)


@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    return users.delete_user(id)