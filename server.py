from jinja2 import StrictUndefined

from flask import Flask, render_template, url_for, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.security import generate_password_hash, check_password_hash
from model import connect_to_db, db
from forms import LoginForm, RegisterForm


app = Flask(__name__)


app.config['SECRET_KEY'] = 'dhsdskowlwjj3744394ghheiso45852el'


app.jinja_env.undefined = StrictUndefined


#####################################################################
#############  VIEW FUNCTIONS -- HAVE FORMS  ########################
#####################################################################


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)

@app.route('/info')
def list_info():
    return render_template('info.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/support_group')
def sup_group():
    return render_template('support_group.html')


if __name__ == "__main__":

    app.debug = True
    
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    

    
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')