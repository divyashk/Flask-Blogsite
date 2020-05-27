from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from flaskblog.models import User;

class RegistrationForm( FlaskForm ):      
    username = StringField('Username', validators = [DataRequired(), Length(min = 2, max = 20)]);

    email = StringField('Email', validators = [DataRequired(), Email()]);

    password = PasswordField('Password', validators=[DataRequired()]);

    confirm_password = PasswordField('Confirm Password' , validators = [DataRequired(), EqualTo('password')] );

    submit = SubmitField('Sign up');

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first();
        if user:
            raise ValidationError("User name already taken. Please try again!");

    def validate_email(self, email):
        email = User.query.filter_by(email = email.data).first();
        if email:
            raise ValidationError("Email already taken. Please try again!");

class LoginForm( FlaskForm ):      
   
    email = StringField('Email', validators = [DataRequired(), Email()]);

    password = PasswordField('Password', validators=[DataRequired()]);

    remember = BooleanField('Remember me');
    submit = SubmitField('Login');

