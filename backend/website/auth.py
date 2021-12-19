from flask import Blueprint

# same idea as views, but auth separate

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return '<p>Login</p>'

@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

@auth.route('/sign-up')
def signup():
    return '<p>Sign Up</p>'


