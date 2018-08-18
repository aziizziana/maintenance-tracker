from flask import request, make_response, jsonify
from app.model.user import User
from app.model.request import Request
from app.application import Application
from . import app

application = Application()


@app.route('/')
def home():
    return 'Welcome home'


@app.route('/register', methods=['POST'])
def register():
    if request.content_type != 'application/json':
        return make_response(jsonify({
            "message": "Please use json as content type"
        })), 400

    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')
    is_admin = data.get('isAdmin')
    user = User(name, email, password, is_admin)
    application.register(user)
    return make_response(jsonify({
        'message': 'successfully registered the user'
    })), 201


@app.route('/login', methods=['POST'])
def login():
    if request.content_type != 'application/json':
        return make_response(jsonify({
            "message": "Please use json as content type"
        })), 400

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not application.does_user_exist(email):
        return make_response(jsonify({
            "message": 'User does not exist'
        })), 400

    if not application.login(email, password):
        return make_response(jsonify({
            "message": "Your password is invalid/wrong"
        })), 400

    user = application.get_user(email)
    token = user.get_token()
    print(token)
    return make_response(jsonify({
        'message': 'succefully logged in',
        'token': token
    })), 200


@app.route('/users/requests', methods=['POST'])
def create_request():
    """
    Move the methods below to a decorator to avoid code duplication
    :return:
    """
    if request.content_type != 'application/json':
        return make_response(jsonify({
            "message": "Please use json as content type"
        })), 400

    if 'Authorization' not in request.headers:
        return make_response(jsonify({
            'message': "Token missing"
        })), 400

    try:
        token = request.headers['Authorization'].split(" ")[1]
    except IndexError:
        return make_response(jsonify({
            "message": "token is missing"
        })), 400

    if isinstance(User.decode(token), str):
        return make_response(jsonify({
            'message': User.decode(token)
        })), 400

    email = User.decode(token)['email']
    data = request.get_json()
    name = data.get('name')
    req = Request(application.generate_random_key(), name, email)
    application.add_request(req)
    return make_response(jsonify({
        'message': 'request added successfully',
        'request': req.get_dict()
    })), 201
