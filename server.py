from flask_login import login_required, login_user, login_manager, logout_user
from jinja2 import StrictUndefined

from flask import Flask, render_template, url_for, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.security import generate_password_hash, check_password_hash
from model import connect_to_db, db, User
from forms import LoginForm, RegisterForm


app = Flask(__name__)


app.config['SECRET_KEY'] = 'dhsdskowlwjj3744394ghheiso45852el'


app.jinja_env.undefined = StrictUndefined


#####################################################################
#############  VIEW FUNCTIONS -- HAVE FORMS  ########################
#####################################################################


@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/', methods=['POST'])
def login_post():
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(name=name).first()

    if user and check_password_hash(user.password, password):
        login_user(user)
        return redirect(url_for('home')) 
    else:
        flash('Check login details and try again')
        return redirect(url_for('login'))

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)

@app.route('/register', methods=['POST'])
def register_post():
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(name=name).first()

    if user:
        flash('Username already exists')
        return redirect(url_for('register'))
    
    new_user = User(name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login'))

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/info')
@login_required
def list_info():
    return render_template('info.html')

@app.route('/resources')
@login_required
def resources():
    return render_template('resources.html')

@app.route('/support_group')
@login_required
def sup_group():
    return render_template('support_group.html')


if __name__ == "__main__":

    app.debug = True
    
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    

    
    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')