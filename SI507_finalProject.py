from flask import Flask, render_template, session, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
import pandas as pd
import csv
from SI507project_tools import *

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.debug = True

clean_movies = pd.read_csv('movies_clean.csv', encoding='utf8')

# Routes
@app.route('/')
def home():
    # total = len(clean_movies.index)
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/superhero')
def superhero():
    return "<h1>This is the all superheroes page.</h1>"

@app.route('/superhero/<name>')
def a_superhero(name):
    return "<h1>This is the specific superhero page.</h1>"

@app.route('/movie')
def movie():
    return "<h1>This is the all movies page.</h1>"

@app.route('/movie/<title>')
def the_movie(title):
    pass

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
	app.run()
