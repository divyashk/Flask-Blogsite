from flask import Flask;
from flask import render_template;
from flask import url_for;
from flask import flash, redirect;

from forms import RegistrationForm, LoginForm

app = Flask( __name__ );  '''creates an object named app of class Flask'''

app.config['SECRET_KEY'] = '479ac0a34b4290c30baffefc740a1d5b';

posts = [
        {
            'author': "Divyasheel", 
            'title': "Blog Site",
            'content': "First Post content",
            'date_posted':"April 20, 2018"
        },
        {
            'author': "Divyasheel 2", 
            'title': "Blog Site 2",
            'content': "Second Post content",
            'date_posted':"April 21, 2018"
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