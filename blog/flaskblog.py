from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def hello_world():
    return render_template('home.html', posts=posts)


# About Page
@app.route('/about')
def about():
    return render_template('about.html', title='')


if __name__ == '__main__':
    app.run(debug=True)
