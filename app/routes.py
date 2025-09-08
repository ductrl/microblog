from flask import render_template, flash, redirect, get_flashed_messages, url_for
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # return True if the browser sends a POST request but False if the browser sends a GET request
        flash(f'Login requested for user {form.username.data}, remember_me = {form.remember_me.data}')
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)