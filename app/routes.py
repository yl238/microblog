# This allows rendering the HTML from a template instead of having all the code here.
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/') # Python decorators. Modifies the function that follows it. 
@app.route('/index') 
# A common pattern is to use them to register functions as callbacks for certain events. 
# The @app.route decorator creates an association between the URL given as an argument and the function.
# This means that when a web browser requires either of these two URLs, Flask is going to invoke
# this function and pass the return value of it back to the browser as a response.
def index():
    
    user = {'username': 'Sue'}

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
    # Invokes the Jinja2 template engine that substitutes the {{...}} blocks with corresponding values
    return render_template('index.html', title='Home', user=user, posts=posts) 

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

    