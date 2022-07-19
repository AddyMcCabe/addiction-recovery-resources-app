from flask_login import login_required, login_user, login_manager, logout_user
from jinja2 import StrictUndefined

from flask import Flask, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from model import connect_to_db, db, User, Group, Resource
from forms import LoginForm, RegisterForm, AddResourceForm, AddGroupForm
import os

app = Flask(__name__)


app.config['SECRET_KEY'] = 'dhsdskowlwjj3744394ghheiso45852el'


app.jinja_env.undefined = StrictUndefined


#####################################################################
#############  VIEW FUNCTIONS -- HAVE FORMS  ########################
#####################################################################

@app.before_first_request
def create_table():
    db.create_all()

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

@app.route('/resources', methods=['GET'])
@login_required
def resources():
    form = AddResourceForm()
    resources = Resource.query.all()
    return render_template('resources.html', resources=resources, form=form)

@app.route('/resources', methods=['POST'])
@login_required
def resources_post():
    form = AddResourceForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        link = form.link.data

        new_resource = Resource(title=title, description=description, link=link)
        db.session.add(new_resource)
        db.session.commit()
        resources = Resource.query.all()
       
        return redirect(url_for('resources'))
    else:
         flash('Make sure all entries are valid')
         return render_template('resources.html', resources=resources, form=form)

@app.route('/support_group', methods=['GET'])
@login_required
def sup_group():
    form = AddGroupForm()
    groups = Group.query.all()
    return render_template('support_group.html', groups=groups, form=form)

@app.route('/support_group', methods=['POST'])
@login_required
def sup_group_post():
    form = AddGroupForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        link = form.link.data

        new_group = Group(name=name, description=description, link=link)
        db.session.add(new_group)
        db.session.commit()
        groups = Group.query.all()

        return redirect(url_for('support_group'))
    else:
        flash('make sure all entries are valid')
        return render_template('support_group.html', groups=groups, form=form)


if __name__ == "__main__":

    # app.debug = True
    
    # app.jinja_env.auto_reload = app.debug


    connect_to_db(app)

    

    

    app.run(port=5000, host='0.0.0.0')