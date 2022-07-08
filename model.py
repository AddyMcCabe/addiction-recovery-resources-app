from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()



















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
