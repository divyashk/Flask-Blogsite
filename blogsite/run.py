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

db = SQLAlchemy(app);                                                          '''creates an object named db which is instance of class SQLAlchemy'''
from models import User, Post


posts=[
    {
        'author':"User 1", 
        'title':"Blog Post 1",
        'content':"First post Content",
        'date_posted':"April 20, 2020"
    },
    {
        'author':"User 2",
        'title':"Blog Post 2",
        'content':"Second Post content",
        'date_posted':"April 21,2020"
    }
]


@app.route("/")        
def home():
    return render_template('home.html', title = "Home" ,posts = posts);  

@app.route("/about")
def about():
    return render_template('about.html', title = "About");

@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegistrationForm();
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'));
    return render_template('register.html', title = 'Register' , form = form);


@app.route("/login", methods= ["GET", "POST"])
def login():
    form = LoginForm();
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash( "You have been logged in !", "success");
            return redirect(url_for("home"));
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
 
    return render_template('login.html', title = 'Login' , form = form);

if __name__ =="__main__":
    app.run(debug=True)