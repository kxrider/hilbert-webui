from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

# same idea as views, but auth separate

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        #check if info is valid
        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='e')
        elif len(firstName) < 2:
            flash('First name must be at least 2 characters', category='e')
        elif password1 != password2:
            flash('Passwords do not match', category='e')
        elif len(password1) < 7:
            flash('Password too short', category='e')
        else:
            # add user to database
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='s')
            return redirect(url_for('views.home'))
            
            
    return render_template('sign_up.html')


