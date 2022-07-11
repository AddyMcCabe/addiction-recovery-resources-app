from jinja2 import StrictUndefined

from flask import Flask, render_template, url_for, redirect
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db


app = Flask(__name__)


app.secret_key = "ABC"


app.jinja_env.undefined = StrictUndefined


#####################################################################
#############  VIEW FUNCTIONS -- HAVE FORMS  ########################
#####################################################################

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/info')
def list_info():
    return render_template('info.html')


if __name__ == "__main__":

    app.debug = True
    
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')