from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField,BooleanField, PasswordField, SubmitField, TextAreaField;
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from flaskblog.models import User;
from flask_wtf.file import FileField, FileAllowed;


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
        user = User.query.filter_by(email = email.data).first();
        if user:
            raise ValidationError("Email already taken. Please try again!");

class LoginForm( FlaskForm ):      
   
    email = StringField('Email', validators = [DataRequired(), Email()]);

    password = PasswordField('Password', validators=[DataRequired()]);

    remember = BooleanField('Remember me');
    submit = SubmitField('Login');

class UpdateAccountForm( FlaskForm ):      
    username = StringField('Username', validators = [DataRequired(), Length(min = 2, max = 20)]);

    email = StringField('Email', validators = [DataRequired(), Email()]);
    picture =  FileField("Update Profile picture", validators=[FileAllowed(['jpg','png'])]);
    submit = SubmitField('Update');

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first();
            if user:
                raise ValidationError("User name already taken. Please try again!");

    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email = email.data).first();
            if email:
                raise ValidationError("Email already taken. Please try again!");

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()]);
    content = TextAreaField("Content", validators=[DataRequired()]);
    submit = SubmitField("Post")

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()]);
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first();
        if user is None:
            raise ValidationError("There is no account with that email, please register!");
    submit = SubmitField("Request Password reset")


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Reset Password")