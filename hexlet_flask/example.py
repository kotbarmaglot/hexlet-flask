from flask import Flask, render_template, request

app = Flask(__name__)

users = ['mike', 'mishel', 'adel', 'keks', 'kamila']

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/users/<id>')
# def user(id):
#     name = id
#     return render_template('users/show.html', name=name)

@app.route('/users/')
def show_users():
    term = request.args.get('term', default=None)
    if not term:
        out_list = users
    else:
        out_list = filter(lambda x: term in x, users)

    return render_template('users/show.html', names=out_list, first_name='aa')
    