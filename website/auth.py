from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.form == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than four characters.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character.', category='error')
        elif password != password2:
            flash('Passwords do not match', category='error')
        elif len(password) < 7:
            flash('Password must be atleast 7 characters', category='error')
        else:
            flash('Account created Successfully', category='success')
    return render_template('signup.html')

