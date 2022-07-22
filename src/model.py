from enum import unique
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
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
    information = db.relationship("Info")
    resources = db.relationship("Resource")
    support_groups = db.relationship("Group")


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
    description = db.Column(db.String(500))
    link = db.Column(db.String(500))
    user_id = db.Column(db.Integer, ForeignKey("users.id"))

class Group(db.Model):

    __tablename__ = 'support_groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    link = db.Column(db.String(500))
    user_id = db.Column(db.Integer, ForeignKey("users.id"))

    





# if __name__ == "__main__":

#     from src import app
#     print("Connected to DB.")
