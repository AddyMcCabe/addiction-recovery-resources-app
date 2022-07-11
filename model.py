from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, redirect
import os


db = SQLAlchemy()

######################################################################
#########################  MODELS  ###################################
######################################################################
 
class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

















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
