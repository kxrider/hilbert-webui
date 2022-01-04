from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from .models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(firstName=user_id).first()

def load_all_users():
    return User.query.all()

# this is where we put "routes" i.e. the pages our user can visit

# define that this is a blueprint
views = Blueprint('views', __name__)

#define a view/blueprint. @ symbol is called a 'decorator'
@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user, userName=current_user.firstName)

@views.route('/aussie')
@login_required
def aussie():
    return render_template('aussie.html', user=current_user, userName=current_user.firstName)

@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user, userName=current_user.firstName)

@views.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if current_user.admin:
        users = load_all_users()
        if request.method == 'POST':
            test = request.form.get('test')
            flash(test, category="s")

        return render_template('admin.html', user=current_user, userName=current_user.firstName, userlist=users)
    else:
        flash("Error! You are not an administrator and thus cannot access this page. Please contact one of the admins for assistance.", category="e")
        return render_template('failure.html', user=current_user, userName=current_user.firstName)
