from flask.ext.lastuser.sqlalchemy import UserBase2
from coaster.sqlalchemy import BaseMixin
from . import db

__all__ = ['User', 'Post']

class User(UserBase2, db.Model):
    __tablename__ = 'user'
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<name {}>'.format(self.name)
        
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Post {}>'.format(self.body)