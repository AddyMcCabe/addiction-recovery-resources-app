from enum import unique
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager, UserMixin
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

    
def connect_to_db(app):
    """Connect the database to our Flask app."""

    
    password = os.environ.get('PASSWORD')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.app = app
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))





if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
