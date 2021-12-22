from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# same idea as views, but auth separate

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Successfully logged in!', category='s')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password.', category='e')
        else:
            flash('User with this email does not exist', category='e')
    
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully logged out.', category='s')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        #check if info is valid
        user = User.query.filter_by(email=email).first()
        if user:
            flash('User with this email already exists.', category='e')
        elif len(email) < 4:
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
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
            
            
    return render_template('sign_up.html', user=current_user)


