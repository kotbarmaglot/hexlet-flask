from flask import Flask, render_template, request

from data import generate_users

users = generate_users(100)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users_post():
    user = {'name': '',
            'email': '',
            'password': '',
            'passwordConfirmation': '',
            'city': ''}
    errors = {}

    return render_template(
        'users/new.html',
        user=user,
        errors=errors

    )



@app.route('/users/new')
def users_new():
    user = {'name': '',
            'email': '',
            'password': '',
            'passwordConfirmation': '',
            'city': ''}
    errors = {}

    return render_template(
        'users/new.html',
        user=user,
        errors=errors
    )