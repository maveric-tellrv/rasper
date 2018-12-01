 
from datetime import datetime

# from views import db
from sqlalchemy import desc

from thermos import db


# db = SQLAlchemy(app)

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text,nullable=False)
    date = db.Column(db.DateTime,default=datetime.utcnow)
    description = db.Column(db.String(3000))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)


    @staticmethod
    def newest(num):
        return  Bookmark.query.order_by(desc(Bookmark.date)).limit(num)

    def __repr__(self):	
        return '<Url %r>' % self.url

    


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    bookmark = db.relationship('Bookmark',backref='user',lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.username