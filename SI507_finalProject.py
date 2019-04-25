from flask import Flask, render_template, session, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
import pandas as pd
import csv
from SI507project_tools import MarvelHero


app = Flask(__name__)
bootstrap = Bootstrap(app)

clean_movies = pd.read_csv('movies_clean.csv', encoding='utf8')

# Routes
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('superhero', name=request.form.get('name')))
    return render_template('index.html')

@app.route('/all_superhero')
def all_superhero():
    return render_template('all_superhero.html')

@app.route('/superhero/<name>')
def superhero(name):
    return render_template('superhero.html', name=name)

@app.route('/all_movie')
def all_movie():
    return render_template('all_movie.html')

@app.route('/movie/<title>')
def movie(title):
    return render_template('movie.html', user_template=title)

@app.route('/a')
def url_for_a():
    return 'here is a'

@app.route('/b')
def b():
    #  所得結果為'/a'
    return redirect(url_for('url_for_a'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

###### Example
@app.route('/loginurl', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if login_check(request.form['username'], request.form['password']):
            flash('Login Success!')
            return redirect(url_for('hello', username=request.form.get('username')))
    return render_template('login.html')

def login_check(username, password):
    if username == 'admin' and password == 'hello':
        return True
    else:
        return False

@app.route('/hello/<username>')
def hello(username):
    return render_template('hello.html', username=username)
###### End of example

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "Your Key"
    app.run()
