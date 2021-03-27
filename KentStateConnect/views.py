"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, session
from flask_mysqldb import MySQL
from flask_mail import Mail, Message
import MySQLdb.cursors
import re 
import uuid
from KentStateConnect import app


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact Us',
        year=datetime.now().year,
        message='Find us at Kent State in the Computer Science department.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About Kent State Connect',
        year=datetime.now().year,
        message='For students, by students.'
    )

@app.route('/resources')
def resources():
    """Renders the Resources page."""
    return render_template(
        'resources.html',
        title='Resources',
        year=datetime.now().year,
        message='Below are some additional links to help you connect with Kent State and other students.'
    )

@app.route('/forum')
def forum():
    """Renders the Forum page."""
    return render_template(
        'forum.html',
        title='Forum',
        year=datetime.now().year,
        message='The forum is currently under development.'
    )

@app.route('/tutors')
def tutors():
    """Renders the Forum page."""
    return render_template(
        'tutors.html',
        title='Tutors',
        year=datetime.now().year,
        message='Due to the ongoing pandemic, tutoring will only be held online through Blackboard Collab between 9am to 9pm EST.'
    )

# main config and Initializing MySQl
app.secret_key = '12345'  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ksc'
app.config['threaded']= True
mysql = MySQL(app) 



# mail settings
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'kentstateconnect@gmail.com'
app.config['MAIL_PASSWORD'] = 'ksc2021!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Intialize Mail
mail = Mail(app)

# Enable account activation?
account_activation_required = True

  
@app.route('/') 
@app.route('/login', methods =['GET', 'POST']) 
def login(): 
    msg = '' 
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form: 
        username = request.form['username'] 
        user_pass = request.form['password'] 
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM users WHERE username = % s AND user_pass = % s', (username, user_pass, )) 
        account = cursor.fetchone() 
        if account: 
            session['loggedin'] = True
            session['user_id'] = account['user_id'] 
            session['username'] = account['username'] 
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg) 
        else: 
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg) 
  
@app.route('/logout') 
def logout(): 
    session.pop('loggedin', None) 
    session.pop('id', None) 
    session.pop('username', None) 
    return redirect(url_for('login')) 
  
@app.route('/register', methods =['GET', 'POST']) 
def register(): 
    msg = '' 
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form : 
        username = request.form['username'] 
        user_pass = request.form['password'] 
        user_email = request.form['email'] 
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM users WHERE username = % s', (username, )) 
        account = cursor.fetchone() 
        if account: 
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', user_email): 
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username): 
            msg = 'Username must contain only characters and numbers!'
        elif not username or not user_pass or not user_email: 
            msg = 'Registration failed.'
        elif account_activation_required: 
            activation_code = uuid.uuid4() # Generate a random unique id for activation code
            cursor.execute('INSERT INTO users VALUES (NULL, % s, % s, % s, % s, FALSE, NULL, NULL, % s)', (username, user_pass, user_email, formatted_date, activation_code)) 
            mysql.connection.commit() 
            email_info = Message('Account Activation Required', sender = 'kentstateconnect@gmail.com', recipients = [user_email])
            activate_link = 'http://localhost:5555/activate/' + str(user_email) + '/' + str(activation_code)
            email_info.body = '<p>Please click the following link to activate your account: <a href="' + str(activate_link) + '">' + str(activate_link) + '</a></p>'
            mail.send(email_info)
            msg = 'Please check your email to activate your account!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into users table
            cursor.execute('INSERT INTO users VALUES (NULL, % s, % s, % s, % s, FALSE, NULL, NULL, % s)', (username, user_pass, user_email, formatted_date, activation_code))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST': 
        msg = 'Registration failed. Please fill out the form and try again.'
    return render_template('register.html', msg = msg) 

# http://localhost:5555/activate/<email>/<code> - this page will activate a users account if the correct activation code and email are provided
@app.route('/activate/<string:user_email>/<string:code>', methods=['GET'])
def activate(user_email, code):
    # Check if the email and code provided exist in the accounts table
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE user_email = %s AND activation_code = %s', (user_email, code,))
    account = cursor.fetchone()
    if account:
        # account exists, update the activation code to "activated"
        cursor.execute('UPDATE users SET activation_code = "activated" WHERE user_email = %s AND activation_code = %s', (user_email, code,))
        mysql.connection.commit()
        # print message, or you could redirect to the login page...
        msg = "Account successfully activated."
        return render_template('index.html', msg = msg)
    return 'Account doesn\'t exist with that email or incorrect activation code!'
