from flask import Flask;
from flask import render_template;
from flask import url_for;
from flask import flash, redirect;
from flask_sqlalchemy import SQLAlchemy;


from forms import RegistrationForm, LoginForm

from datetime import datetime

app = Flask( __name__ );                                                       '''creates an object named app of class Flask'''
app.config['SECRET_KEY'] = '479ac0a34b4290c30baffefc740a1d5b';
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db';                   '''stores the site.db database at the current working directory'''

db = SQLAlchemy(app);                