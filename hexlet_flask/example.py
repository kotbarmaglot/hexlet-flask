from flask import Flask, render_template, request

from data import generate_users

users = generate_users(100)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users/')
def show_users():
    term = request.args.get('term', default=None)
    out_list = []
    in_list = []

    if not term:
        for elem in users:
            out_list.append(elem.get('first_name'))
        return render_template('users/index.html', names=out_list)
    else:
        for elem in users:
            nol = elem.get('first_name').lower()
            if nol[0].find(term[0].lower()) == 0:
            
                in_list.append(elem.get('first_name'))


        out_list  = filter(lambda x: term.lower() in x.lower(), in_list)

        return render_template('users/index.html', names=out_list, first_name=term)