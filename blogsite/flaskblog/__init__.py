from flask import Flask;
from flask_bcrypt import Bcrypt;
from flask_sqlalchemy import SQLAlchemy;
from flask_login import LoginManager;




app = Flask( __name__ );                                                       '''creates an object named app of class Flask'''
app.config['SECRET_KEY'] = '479ac0a34b4290c30baffefc740a1d5b';
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db';                   '''stores the site.db database at the current working directory'''

db = SQLAlchemy(app);      
bcrypt = Bcrypt(app);
login_manager = LoginManager(app);
login_manager.login_view = "login";
login_manager.login_message_category = "info";

from flaskblog import routes;
