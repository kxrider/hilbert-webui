from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user

# this is where we put "routes" i.e. the pages our user can visit

# define that this is a blueprint
views = Blueprint('views', __name__)

#define a view/blueprint. @ symbol is called a 'decorator'
@views.route('/')
@login_required
def home():
    #return '<h1>Test</h1>'
    return render_template('home.html', user=current_user, userName = current_user.firstName)

@views.route('/aussie')
@login_required
def aussie():
    return render_template('aussie.html', user=current_user, userName = current_user.firstName)

@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user, userName = current_user.firstName)
