"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
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