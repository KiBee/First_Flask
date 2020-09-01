from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from ilh import db, app
from ilh.models import Message, User


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', messages=Message.query.all())


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    db.session.add(Message(text, tag))
    db.session.commit()

    return redirect(url_for('main'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = User.query.filter_by(login=login).first()
        if check_password_hash(user.password, password):
            login_user(user)

            next_page = request.args.get('next')

            redirect(next_page)
        else:
            flash('Login or password is not correct')
    else:
        flash('Please fill login and password fields')
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    pass


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    pass
