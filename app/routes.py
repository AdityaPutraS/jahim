from flask import *
from app import app
from app.forms import LoginForm,RegisterForm

@app.route('/')
def index():
    return render_template('main.html',judul = 'Main')
@app.route('/main')
def main():
    return render_template('main.html',judul = 'Main')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('{}'.format(
            form.username.data))
        return redirect(url_for('main'))
    return render_template('login.html', judul='Login', form=form)
@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('{}'.format(
            form.username.data))
        return redirect(url_for('main'))

    return render_template('register.html', judul='Register', form=form)
@app.route('/search', methods=['GET','POST'])
def search():
    return render_template('search.html',judul='Search')
