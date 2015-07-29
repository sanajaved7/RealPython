#controller for application

#imports
from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3

#configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = '\xde\x86\xb8\x17\xf0\x0cw\xcd22m\xf7\x84\x9d\xf1:U\xe0eW\x03\xd0\xcc\xa4'

app = Flask(__name__)

#pulls in config by looking for uppercase variables
app.config.from_object(__name__)

#function to connect to database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
                error = 'Invalid Credentials. Please try again.'
        else:
            session['logged in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
