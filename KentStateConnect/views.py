"""
Routes and views for the flask application.
"""

import datetime , sqlite3
from flask import Flask, render_template, redirect, url_for, request, session, make_response
from flask_mail import Mail, Message
import re , uuid , hashlib, os
from KentStateConnect import app



@app.route('/contact')
def contact():
	"""Renders the contact page."""
	return render_template(
		'contact.html',
		title='Contact Us',
		message='Find us at Kent State in the Computer Science department.'
	)

@app.route('/about')
def about():
	"""Renders the about page."""
	return render_template(
		'about.html',
		title='About Kent State Connect',
		message='For students, by students.'
	)

@app.route('/resources')
def resources():
	"""Renders the Resources page."""
	return render_template(
		'resources.html',
		title='Resources',
		message='Below are some additional links to help you connect with Kent State and other students.'
	)

@app.route('/forum')
def forum():
	if loggedin():
		"""Renders the Forum page."""
		return redirect('http://localhost:8000')
	return render_template('login.html')

@app.route('/tutors')
def tutors():
	"""Renders the Forum page."""
	return render_template(
		'tutors.html',
		title='Tutors',
		message='Due to the ongoing pandemic, tutoring will only be held online through Blackboard Collab between 9am to 9pm EST.'
	)

# main config and Initializing SQLite Database
connection = sqlite3.connect('db.sqlite3', check_same_thread=False)
app.secret_key = '12345'  
app.config['threaded']= True

# Enter your domain name below
app.config['DOMAIN'] = 'http://localhost:5555'

# mail settings
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'kentstateconnect@gmail.com'
app.config['MAIL_PASSWORD'] = 'Capstoneproject!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Intialize Mail
mail = Mail(app)


# Enable account activation?
account_activation_required = True

# Enable CSRF Protection?
csrf_protection = False

# This will be the home page, only accessible for loggedin users
@app.route('/')
@app.route('/home')
def home():
	# Check if user is loggedin
	if loggedin():
		# User is loggedin show them the home page
		return render_template('home.html', username=session['username'])
	# User is not loggedin redirect to login page
	return render_template('login.html')


@app.route('/login', methods =['GET', 'POST']) 
def login(): 
	# Redirect user to home page if logged-in
	if loggedin():
		return redirect(url_for('home'))
	# Output message if something goes wrong...
	msg = ' ' 
	# Checks if "username" and "password" POST requests exist (user submitted form)
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form: 
		# Create variables for ease of use
		username = request.form['username'] 
		password = request.form['password'] 
		# Retrieving hashed password
		hash =	password + app.secret_key
		hash = hashlib.sha1(hash.encode())
		password = hash.hexdigest();
		# Check if account exists using MySQL
		cursor = connection.cursor() 
		cursor.execute('SELECT * FROM auth_user WHERE username = ? AND password = ?', (username, password))
		# Fetch record and return result
		account = cursor.fetchone() 
		if account: 
			# If account exists in users table in the database
			if account_activation_required and account[8] != 'activated' and account[8] != '':
				return 'Please activate your account to login!'
			# Create session data, we can access this data in other routes
			session['loggedin'] = True
			session['user_id'] = account[0] 
			session['username'] = account[2] 
			if 'rememberme' in request.form:
				# Create hash to store as cookie
				hash = request.form['password'] + app.secret_key
				hash = hashlib.sha1(hash.encode())
				hash = hash.hexdigest();
				# The cookie expires in 30 days
				expire_date = datetime.datetime.now() + datetime.timedelta(days=30)
				resp = make_response('Success.', 200)
				resp.set_cookie('rememberme', hash, expires=expire_date)
				# Update rememberme in accounts table to the cookie hash
				cursor.execute('UPDATE auth_user SET rememberme = ? WHERE user_id = ?', (hash, account[0],))
				connection.commit()
				return resp
			return 'Success'
		else: 
			msg = 'Incorrect username / password!'
	return render_template('login.html', msg = msg) 

# Check if logged in, update session if cookie for "remember me" exists 
def loggedin():
	if 'loggedin' in session:
		return True
	elif 'rememberme' in request.cookies:
		cursor = connection.cursor()
		# Check if remembered, cookie has to match the "rememberme" field
		cursor.execute('SELECT * FROM auth_user WHERE rememberme = ?', (request.cookies['rememberme'],))
		account = cursor.fetchone()
		if account:
			# Update session variables
			session['loggedin'] = True
			session['user_id'] = account[0]
			session['username'] = account[2]
			return True
	# Account not logged in returns false
	return False

@app.route('/logout') 
def logout(): 
	session.pop('loggedin', None) 
	session.pop('id', None) 
	session.pop('username', None) 
	# Remove cookie data "remember me"
	resp = make_response(render_template('login.html'))
	resp.set_cookie('rememberme', expires=0)
	return resp

@app.route('/register', methods =['GET', 'POST']) 
def register(): 
	msg = '' 
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form : 
		username = request.form['username'] 
		password = request.form['password'] 
		cpassword = request.form['cpassword']
		KSUID = request.form['email']
		user_email = KSUID + "@kent.edu"
		#now = datetime.now()
		# Hash the password
		hash = password + app.secret_key
		hash = hashlib.sha1(hash.encode())
		hashed_password = hash.hexdigest();
		# Checking if account exists 
		cursor = connection.cursor() 
		cursor.execute('SELECT * FROM auth_user WHERE username = ?', (username,)) 
		account = cursor.fetchone() 
		if account: 
			msg = 'Account already exists!'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', user_email): 
			msg = 'Invalid email address!'
		elif not re.match(r'[A-Za-z0-9]+', username): 
			msg = 'Username must contain only characters and numbers!'
		elif not username or not password or not user_email: 
			msg = 'Registration failed.'
		elif password != cpassword:
			return 'Passwords do not match!'
		elif account_activation_required: 
			activation_code = uuid.uuid4() # Generate a random unique id for activation code
			cursor.execute('INSERT INTO auth_user (username, password, user_email, activation_code) VALUES  (?, ?, ?, ?)', (username, hashed_password, user_email, str(activation_code))) 
			connection.commit() 
			email_info = Message('Account Activation Required', sender = 'kentstateconnect@gmail.com', recipients = [user_email])
			activate_link = app.config['DOMAIN'] + url_for('activate', user_email=user_email, code=str(activation_code))
			# Define and render the activation email template
			email_info.body = render_template('activation-email-template.html', link=activate_link)
			email_info.html = render_template('activation-email-template.html', link=activate_link)
			# send activation email to user
			mail.send(email_info)
			msg = 'Please check your email to activate your account!'
		else:
			# Account doesnt exists and the form data is valid, now insert new account into users table
			cursor.execute('INSERT INTO auth_user (username, password, user_email, activation_code) VALUES  (?, ?, ?, ?)', (username, hashed_password, user_email, str(activation_code))) 
			connection.commit()
			msg = 'You have successfully registered!'
	elif request.method == 'POST': 
		msg = 'Registration failed. Please fill out the form and try again.'
	return render_template('register.html', msg = msg) 

# http://localhost:5555/activate/<email>/<code> - this page will activate a users account if the correct activation code and email are provided
@app.route('/activate/<string:user_email>/<string:code>', methods=['GET'])
def activate(user_email, code):
	# Check if the email and code provided exist in the accounts table
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM auth_user WHERE user_email = ? AND activation_code = ?', (user_email, code,))
	account = cursor.fetchone()
	if account:
		# account exists, update the activation code to "activated"
		cursor.execute('UPDATE auth_user SET activation_code = "activated" WHERE user_email = ? AND activation_code = ?', (user_email, code,))
		connection.commit()
		# print message, or you could redirect to the login page...
		msg = "Account successfully activated."
		return render_template('home.html', msg = msg)
	return 'Account doesn\'t exist with that email or incorrect activation code!'

# This will be the profile page, only accessible for loggedin users
@app.route('/profile')
def profile():
	# Check if user is loggedin
	if loggedin():
		# Need to grab the account info for the user so it can be displayed on the profile page
		cursor = connection.cursor()
		cursor.execute('SELECT * FROM auth_user WHERE user_id = ?', (session['user_id'],))
		account = cursor.fetchone()
		# Show the profile page with account info
		return render_template('profile.html', account=account)
	# User is not loggedin redirect to login page
	return redirect(url_for('login'))

# User can edit their existing details
@app.route('/profile/edit', methods=['GET', 'POST'])
def edit_profile():
	# Check if user is loggedin
	if loggedin():
		# We need all the account info for the user so we can display it on the profile page
		cursor = connection.cursor()
		# Output message
		msg = ''
		# Check if "username", "password" and "email" POST requests exist (user submitted form)
		if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
			# Create variables for easy access
			username = request.form['username']
			password = request.form['password']
			user_email = request.form['email']
			# Retrieve account by the username
			cursor.execute('SELECT * FROM auth_user WHERE username = ?', (username,))
			account = cursor.fetchone()
			# validation check
			if not re.match(r'[^@]+@[^@]+\.[^@]+', user_email):
				msg = 'Invalid email address!'
			elif not re.match(r'[A-Za-z0-9]+', username):
				msg = 'Username must contain only characters and numbers!'
			elif not username or not user_email:
				msg = 'Please fill out the form!'
			elif session['username'] != username and account:
				msg = 'Username already exists!'
			else:
				cursor.execute('SELECT * FROM auth_user WHERE user_id = ?', (session['user_id'],))
				account = cursor.fetchone()
				current_password = account[1]
				if password:
					# Hash the password
					hash = password + app.secret_key
					hash = hashlib.sha1(hash.encode())
					current_password = hash.hexdigest();
				# Update account with the new details
				cursor.execute('UPDATE auth_user SET username = ?, password = ?, user_email = ? WHERE user_id = ?', (username, current_password, user_email, session['user_id'],))
				connection.commit()
				msg = 'Updated!'
		cursor.execute('SELECT * FROM auth_user WHERE user_id = ?', (session['user_id'],))
		account = cursor.fetchone()
		# Show the profile page with account info
		return render_template('profile-edit.html', account=account, msg=msg)
	return redirect(url_for('login'))

# http://localhost:5000//forgotpassword - user can use this page if they have forgotten their password
@app.route('/forgotpassword', methods=['GET', 'POST'])
def forgotpassword():
	msg = ''
	if request.method == 'POST' and 'email' in request.form:
		email = request.form['email']
		cursor = connection.cursor()
		cursor.execute('SELECT * FROM auth_user WHERE user_email = ?', (email,))
		account = cursor.fetchone()
		if account:
			# Generate unique ID
			reset_code = uuid.uuid4()
			# Update the reset column in the accounts table to reflect the generated ID
			cursor.execute('UPDATE auth_user SET reset = ? WHERE user_email = ?', (str(reset_code), email,))
			connection.commit()
			email_info = Message('Password Reset', sender = app.config['MAIL_USERNAME'], recipients = [email])
			# Generate reset password link
			reset_link = app.config['DOMAIN'] + url_for('resetpassword', email = email, code = str(reset_code))
			# Email Info
			email_info.body = 'Please click the following link to reset your password: ' + str(reset_link)
			email_info.html = '<p>Please click the following link to reset your password: <a href="' + str(reset_link) + '">' + str(reset_link) + '</a></p>'
			mail.send(email_info)
			msg = 'Reset password link has been sent to your email!'
		else:
			msg = 'An account with that email does not exist!'
	return render_template('forgotpassword.html', msg=msg)

# Proceed to reset the user's password
@app.route('/resetpassword/<string:email>/<string:code>', methods=['GET', 'POST'])
def resetpassword(email, code):
	msg = ''
	cursor = connection.cursor()
	# Retrieve the account with the email and reset code provided from the GET request
	cursor.execute('SELECT * FROM auth_user WHERE user_email = ? AND reset = ?', (email, code,))
	account = cursor.fetchone()
	# If account exists
	if account:
		# Check if the new password fields were submitted
		if request.method == 'POST' and 'npassword' in request.form and 'cpassword' in request.form:
			npassword = request.form['npassword']
			cpassword = request.form['cpassword']
			# Password fields must match
			if npassword == cpassword and npassword != "":
				# Hash new password
				hash = npassword + app.secret_key
				hash = hashlib.sha1(hash.encode())
				npassword = hash.hexdigest();
				# Update the user's password
				cursor.execute('UPDATE auth_user SET password = ?, reset = "" WHERE user_email = ?', (npassword, email,))
				connection.commit()
				msg = 'Your password has been reset, you can now <a href="' + url_for('login') + '">login</a>!'
			else:
				msg = 'Passwords must match and must not be empty!'
		return render_template('resetpassword.html', msg=msg, email=email, code=code)
	return 'Invalid email and/or code!'
