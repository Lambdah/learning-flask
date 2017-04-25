from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class Signup(Form):
    first_name = StringField('First name', validators=[DataRequired("Please enter your First name.")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter your Last name")])
    email = StringField('Email', validators=[DataRequired("Please enter your E-mail"), Email("Please enter your E-mail")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your Password"), Length(min=6, message="Please enter more than 6 characters")])
    submit = SubmitField('Sign up')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your Email"), Email(message="Please enter valid Email")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password.")])
    submit = SubmitField('Sign in')

class AddressForm(Form):
    address = StringField('Address', validators=[DataRequired("Please enter an address")])
    submit = SubmitField("Search")
