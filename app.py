from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from db import add_user, verify_user

#from db import add_user, add_tutor, verify_user, verify_tutor
app = Flask(__name__)

# This initializes the sessions so it can be used across the program
app.config['SESSION_TYPE'] = ("filesystem")
Session(app)

# Render the home page--------------------------------------------------------------------------------------
@app.route("/")
def home():
    return render_template("home.html")

# Render the discover page----------------------------------------------------------------------------------
@app.route("/discover")
def discover():
    return render_template("discover.html")

# Render the tickets page-----------------------------------------------------------------------------------
@app.route("/tickets")
def tickets():
    return render_template("tickets.html")

# Render the about us page----------------------------------------------------------------------------------
@app.route("/about-us")
def aboutus():
    return render_template("aboutus.html")

# Render the support page-----------------------------------------------------------------------------------
@app.route("/support")
def support():
    return render_template("support.html")

# Render the signup page and the functions that come withing the signing up progress------------------------
@app.route('/signup' ,methods = ['GET', 'POST'])
def signup():
    error = None

    if request.method == 'POST':
        action = request.form['action']
        
        if action == 'signup':
            # Get the form data for user registration
            email = request.form['email']
            fname = request.form['fname']
            lname = request.form['sname']
            password = request.form['password']
            # Validate the data
            if email == '' or fname == '' or lname == '' or password =='':
                error = "Missing Credentials"
                return render_template("signup.html", error = error)
            elif email.isspace() or fname.isspace() or lname.isspace() or password.isspace():
                error = "Missing Credentials"
                return render_template("signup.html", error = error)
            elif '@' not in email:
                error = "Email not valid"
                return render_template("signup.html", error = error)
            # Run the function in db.py that will add the user information into the database
            add_user(fname, lname, email, password)
            return render_template("signup.html")
    return render_template("signup.html")

# Render the login page and the functions that come withing the signing up progress--------------------------
@app.route('/login' ,methods = ['GET', 'POST'])
def login():

    if request.method == "POST":
        action = request.form['action']

        if action == 'login':
            email = request.form['email']
            password = request.form['password']
        if verify_user(email, password):
            user = verify_user(email, password)
            session['user']=user
            return render_template('home.html', user = session['user'])
        else:
            return "Invalid credentials"

    else:
        if not session.get('user'):
            return render_template('login.html')
        else:
            return render_template('home.html', user = session['user'])
        
@app.route('/logout', methods=['GET', 'POST'])
def logout_user():
    session.pop('user', None)
    return render_template('home.html')
        

# This is for running the application (can be ignored)
if __name__ == "__main__":
    app.run(debug=True)