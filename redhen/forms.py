from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    pwd = PasswordField('Password', validators=[DataRequired()])
    confirm_pwd = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('pwd')])
    submit = SubmitField('Register')


class LogInForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    pwd = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')