from flask_sqlalchemy import SQLAlchemy

###*********************************************
#sqlalchemy的对象一定要放在models里面来创建
db = SQLAlchemy()

class User1(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(16))


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    u_name = db.Column(db.String(16))
    u_age = db.Column(db.Integer, default=1)


class Movie(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    m_name = db.Column(db.String(256))


class Collect(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    c_user = db.Column(db.Integer, db.ForeignKey(User.id))
    c_movie = db.Column(db.Integer, db.ForeignKey(Movie.id))
