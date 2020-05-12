from flask import Flask;
from flask import render_template;
from flask import url_for;


app = Flask( __name__ );  '''creates an object named app of class Flask'''
                           
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



if __name__ =="__main__":
    app.run(debug=True)