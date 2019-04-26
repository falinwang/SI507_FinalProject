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
association = db.Table('movie',db.Column('distributor_id',db.Integer, db.ForeignKey('distributor.id')),db.Column('character_id',db.Integer, db.ForeignKey('character.id')))

class Character(db.Model):
    __tablename__ = "character"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80))
    thumbnail = db.Column(db.String(80))
    wiki = db.Column(db.String(80))
    movie = db.relationship('Movie',backref='Character')

    def __repr__(self):
        return "{} (ID: {})".format(self.name,self.id)

class Distributor(db.Model):
    __tablename__ = "distributor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    movies = db.relationship('Movie',backref='Distributor')

    def __repr__(self):
        return "{} (ID: {})".format(self.name,self.id)

class Movie(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    distributor_id = db.Column(db.Integer, db.ForeignKey("distributor.id"))
    creative_type = db.Column(db.String(64))
    worldwide_gross = db.Column(db.Integer)
    # character = db.Column(db.String(64), db.ForeignKey("character.id"))

    def __repr__(self):
        return "{} by {}, {}| {}".format(self.title,self.director_id, self.distributor_id, self.genre)

def get_or_create_distributor(distributor_name):
    distributor = Distributor.query.filter_by(name=distributor_name).first()
    if distributor:
        return distributor
    else:
        distributor = Distributor(name=distributor_name)
        session.add(distributor)
        session.commit()
        return distributor

def get_or_create_character(character_name):
    character = Character.query.filter_by(name=character_name).first()
    if character:
        return character
    else:
        character = Character(name=character_name)
        session.add(character)
        session.commit()
        return character

# Form
class FormSearch(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Search')

class FormAddMovie(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    distributor = StringField('Distributor', validators=[DataRequired()])
    character = StringField('Character', validators=[DataRequired()])
    submit = SubmitField('Submit')


# clean_movies = pd.read_csv('movies_clean.csv', encoding='utf8')




# Routes
@app.route('/', methods=['GET', 'POST'])
def home():
    # if request.method == 'POST':
        # return redirect(url_for('superhero', name=request.form.get('name')))
    form = FormSearch()
    if form.validate_on_submit():
        name = form.name.data
        flash('Searched for: %s' % form.name.data)
        searching_hero(name)
        return redirect(url_for('superhero', name=name))
    return render_template('index.html', form=form)

@app.route('/all_superhero')
def all_superhero():
    superheroes = Character.query.all()
    num_superheroes = len(superheroes)
    return render_template('all_superhero.html', num_superheroes=num_superheroes)

@app.route('/superhero/<name>', methods=['GET'])
def superhero(name):
    if request.method == "GET":
        name = request.args.get('name','') # string
    if Character.query.filter_by(name=name).first():
        return "{}".format(get_or_create_character(name).name)
    else:
        return render_template('superhero.html', name=name)

@app.route('/all_movie')
def all_movie():
    movies = Movie.query.all()
    num_movies = len(movies)
    return render_template('all_movie.html', num_movies=num_movies)

@app.route('/add_movie')
def movie():
    form = FormAddMovie()
    return render_template('add_movie.html', form=form)

@app.route('/newmovie_result',methods=["GET"])
def addmovies_result():
    if request.method == "GET":
        title = request.args.get('title','') # string
        director_name = request.args.get('director','') # string
        rate = request.args.get('rating','') # integer
        if Movie.query.filter_by(title = title).first(): # if there is a movie by that title
            return "That movie already exists, return to home page!"
        else: # Add movie, director and rating to database
            director = get_or_create_director(director_name)
            rating = create_rating(rate)
            movie = Movie(title = title, director_id = director.id, ratings_id = rating.id)
            session.add(movie)
            session.commit()
            return "New movie: <b>{}</b> by <b>{}</b>, rating: <b>{}</b>.".format(movie.title, director.name, rating.imdb_rating)

    return "Nothing was submitted yet... <a href='http://localhost:5000/form2'>Go submit something</a>"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


if __name__ == '__main__':
    db.create_all()
    app.debug = True
    app.run()
