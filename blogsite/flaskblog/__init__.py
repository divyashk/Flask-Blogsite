from flask import Flask;

from flask_sqlalchemy import SQLAlchemy;





app = Flask( __name__ );                                                       '''creates an object named app of class Flask'''
app.config['SECRET_KEY'] = '479ac0a34b4290c30baffefc740a1d5b';
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db';                   '''stores the site.db database at the current working directory'''

db = SQLAlchemy(app);      

from flaskblog import routes;
