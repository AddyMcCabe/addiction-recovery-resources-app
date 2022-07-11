from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import UserMixin
from sqlalchemy import ForeignKey


db = SQLAlchemy()

######################################################################
#########################  MODELS  ###################################
######################################################################
 
class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(500))
    information = db.Relationship("Info")
    resources = db.Relationship("Resource")
    support_groups = db.Relationship("Group")


class Info(db.Model):

    __tablename__ = 'information'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    link = db.Column(db.String(500))
    user_id = db.Column(db.Integer, ForeignKey("users.id"))

class Resource(db.Model):

    __tablename__ = 'resources'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    link = db.Column(db.String(500))
    user_id = db.Column(db.Integer, ForeignKey("users.id"))

class Group(db.Model):

    __tablename__ = 'support_groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    link = db.Column(db.String(500))
    user_id = db.Column(db.Integer, ForeignKey("users.id"))
















def connect_to_db(app):
    """Connect the database to our Flask app."""

    
    password = os.environ.get('PASSWORD')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://addis:{password}@localhost:5432/'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
