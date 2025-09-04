from flask import render_template
from app import app
from app import LoginForm

# if the browser requests either of these two IRLs, Flask is going to invoke this function and return values back to the browser
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mike'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title='Yo', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()

    return render_template('login.html', title='Sign In', form=form)