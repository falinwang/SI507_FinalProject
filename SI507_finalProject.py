import os
from flask import Flask, render_template, session, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
import csv
from SI507project_tools import *


app = Flask(__name__)
app.use_reloader = True
app.config['SECRET_KEY'] = 'ji3g4z83xup6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./superhero.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bootstrap = Bootstrap(app)
# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy


# Model
class Superhero(db.Model):
    __tablename__ = "character"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80))
    thumbnail = db.Column(db.String(80))
    wiki = db.Column(db.String(80))

class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    distributor_id = db.Column(db.Integer, db.ForeignKey("distributor.id"))
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    IMDB_rating = db.Column(db.Float)
    creative_type = db.Column(db.String(64))
    worldwide_gross = db.Column(db.Integer)


# Form
class FormSearch(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Search')



clean_movies = pd.read_csv('movies_clean.csv', encoding='utf8')







# Routes
@app.route('/', methods=['GET', 'POST'])
def home():
    # if request.method == 'POST':
        # return redirect(url_for('superhero', name=request.form.get('name')))
    form = FormSearch()
    if form.validate_on_submit():
        name = form.name.data
        flash('Searched for: %s' % form.name.data)
        instance_list = []
        hero_list = get_hero_data_with_caching(name)
        try:
            for superhero in hero_list['data']['results']:
                instance = MarvelHero(superhero)
                instance_list.append(instance)
            flash('Searching for keyword \"{}\" in Marvel database ...' % name)
        except:
            flash("\nSorry, no result matches the keyword. Please try again.")
        else:
            if instance_list != []:
                print("Yay! Here is what I found:")
                print("==================================================================================")
                for i in instance_list:
                    print("\n")
                    print(i)
                    break
            else:
                flash("\nSorry, no result matches the keyword. Please try again.")
        return redirect(url_for('superhero', name=name))
    return render_template('index.html', form=form)

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
