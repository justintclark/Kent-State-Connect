"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
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

  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ksc'
  
mysql = MySQL(app) 
  
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
            session['id'] = account['id'] 
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
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
        cursor.execute('SELECT * FROM users WHERE username = % s', (username, )) 
        account = cursor.fetchone() 
        if account: 
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', user_email): 
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username): 
            msg = 'Username must contain only characters and numbers !'
        elif not username or not user_pass or not user_email: 
            msg = 'Registration failed.'
        else: 
            cursor.execute('INSERT INTO users VALUES (NULL, % s, % s, % s)', (username, user_pass, user_email, )) 
            mysql.connection.commit() 
            msg = 'You have successfully registered !'
    elif request.method == 'POST': 
        msg = 'Registration failed.'
    return render_template('register.html', msg = msg) 