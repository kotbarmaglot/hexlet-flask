from flask import Flask, redirect, render_template, request
# BEGIN (write your solution here)
from hexlet_flask.validator import validate
# END
import os

from hexlet_flask.data import Repository


app = Flask(__name__)
app.config['SECRET_KEY'] = 'filesystem'


repo = Repository()


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/courses')
def courses_get():
    courses = repo.content()
    return render_template(
        'courses/index.html',
        courses=courses,
        )


# BEGIN (write your solution here)
@app.post('/courses')
def courses_post():
    course = request.form.to_dict()
    errors = validate(course)
    if errors:
        return render_template(
            'courses/new.html',
            course=course,
            errors=errors,
        ), 422

    repo.save(course)
    return redirect('/courses', 302)


@app.route('/courses/new')
def courses_new():
    course = {'title': '', 'paid': ''}
    errors = {}
    return render_template(
        'courses/new.html',
        course=course,
        errors=errors,
        )
# END
