from flask import render_template, flash, redirect, url_for
from flaskblog.forms import RegistrationForms, LoginForms
from flaskblog.models import User, Post
from flaskblog import app


posts = [
    {
        'author': 'Kamrul Jaman',
        'title': 'Blog post 1',
        'content': ' This is blog post content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Riaz Uddin',
        'title': 'Blog post 2',
        'content': ' This is blog post content for blog 2',
        'date_posted': 'April 21, 2020'
    }
]


# Home Page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


# About Page
@app.route('/about')
def about():
    return render_template('about.html', title='About')


# User Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForms()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        print('It\'s working')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registration', form=form)


# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForms()
    if form.validate_on_submit():
        if form.email.data == 'kam@gmail.com' and form.password.data == 'pass':
            flash(f'You have been login!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful! Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

