from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegisterForm(FlaskForm):

    name = StringField('Username', validators=[DataRequired(),Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(),])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):

    name = StringField('Username', validators=[DataRequired(),Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AddResourceForm(FlaskForm):

    title = StringField('Name', validators=[DataRequired()])
    description = StringField('About', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddGroupForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])
    description = StringField('About', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()])
    submit = SubmitField('Submit')