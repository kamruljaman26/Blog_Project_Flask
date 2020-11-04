from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForms, LoginForms
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fc5a25862d96ac37fadf1b6ad07c2bc1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


# Post Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


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


if __name__ == '__main__':
    app.run(debug=True)
