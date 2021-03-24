"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re , os
from KentStateConnect import app
from itsdangerous import URLSafeTimedSerializer
from KentStateConnect.email import send_email



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

#main config
app.secret_key = '12345'  
SECURITY_PASSWORD_SALT = 'my_precious_two'
DEBUG = False
BCRYPT_LOG_ROUNDS = 13
WTF_CSRF_ENABLED = True
DEBUG_TB_ENABLED = False
DEBUG_TB_INTERCEPT_REDIRECTS = False
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ksc'
mysql = MySQL(app) 

# mail settings
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True

# gmail authentication
#MAIL_USERNAME = os.environ['MAIL_USERNAME']
#MAIL_PASSWORD = os.environ['MAIL_PASSWORD']

# mail accounts
MAIL_DEFAULT_SENDER = 'from@example.com'
  
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
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', user_email): 
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username): 
            msg = 'Username must contain only characters and numbers !'
        elif not username or not user_pass or not user_email: 
            msg = 'Registration failed.'
        else: 
            cursor.execute('INSERT INTO users VALUES (NULL, % s, % s, % s, % s, FALSE, NULL, NULL)', (username, user_pass, user_email, formatted_date)) 
            mysql.connection.commit() 
            token = generate_confirmation_token(user_email)
            msg = 'You have successfully registered !'
            confirm_url = url_for('confirm_email', token=token, _external=True)
            html = render_template('activate.html', confirm_url=confirm_url)
            subject = "Please confirm your email"
            send_email(user_email, subject, html)
            flash('A confirmation email has been sent via email.', 'success')

    elif request.method == 'POST': 
        msg = 'Registration failed.'
    return render_template('register.html', msg = msg) 



#@app.route('/confirmation', methods =['GET', 'POST']) 
#def generate_confirmation_token(user_email): 
#    msg = '' 
#    if request.method == 'POST' and 'user_email' in request.form: 
#        user_email = request.form['user_email'] 
#        serializer = URLSafeTimedSerializer(app.config['secret_key'])
 #       return serializer.dumps(user_email, salt=app.config['SECURITY_PASSWORD_SALT'])

#def confirm_token(token, expiration=3600):
 #   serializer = URLSafeTimedSerializer(app.config['secret_key'])
  #  if request.method == 'POST' and 'user_email' in request.form: 
   #     user_email = request.form['user_email'] 
    #try:
     #   user_email = serializer.loads(
      #      token,
       #     salt=app.config['SECURITY_PASSWORD_SALT'],
        #    max_age=expiration
        #)
    #except:
     #   return False
    #return user_email

#@app.route('/confirm/<token>')
#def confirm_email(token):
#    if request.method == 'POST' and 'user_email' and 'user_confirmed' and 'user_confirmed_on' in request.form: 
#        user_email = request.form['user_email'] 
#        user_confirmed = request.form['user_confirmed']
#        user_confirmed_on = request.form['user_confirmed_on']
#    try:
#        user_email = confirm_token(token)
#    except:
#        flash('The confirmation link is invalid or has expired.', 'danger')
#    user = User.query.filter_by(email=email).first_or_404()
#    if user.confirmed:
#        flash('Account already confirmed. Please login.', 'success')
#    else:
#        user_confirmed = True
#        user_confirmed_on = datetime.datetime.now()
#        mysql.connection.commit() 
#        flash('You have confirmed your account. Thanks!', 'success')
#    return redirect(url_for('home'))