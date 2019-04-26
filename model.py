from flask_register import db

class UserRegister(db.Model):
    """記錄使用者資料的資料表"""
    __tablename__ = 'UserRegisters'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'username:%s, email:%s' % (self.username, self.email)

class Superhero(db.Model):
    """"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80))
    thumbnail = db.Column(db.String(80))
    wiki = db.Column(db.String(80))




class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    distributor_id = db.Column(db.Integer, db.ForeignKey("distributor.id"))
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    rotten_tomatoes_rating = db.Column(db.Float)
    IMDB_rating = db.Column(db.Float)
    genre = db.Column(db.String(64))
