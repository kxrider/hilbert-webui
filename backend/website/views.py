from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_socketio import SocketIO
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from .models import User
from . import db

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_email):
    return User.query.filter_by(email=user_email).first()

def load_all_users():
    return User.query.all()

def formToBool(x):
    if (x=="on" or x=="True"):
        return True
    elif (x==None or x=="False"):
        return False

# this is where we put "routes" i.e. the pages our user can visit

# define that this is a blueprint
views = Blueprint('views', __name__)

#define a view/blueprint. @ symbol is called a 'decorator'
@views.route('/')
@login_required
def home():
    if current_user.viewConsole:
        return render_template('home.html', user=current_user, userName=current_user.firstName)
    else:
        flash("Woops! You do not have permission to view the server console, please contact and administrator for assistance.", category="e")
        return render_template('failure2.html', user=current_user, userName=current_user.firstName)

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
            userEmail = request.form.get('userEmail')
            modalAdmin = request.form.get('modalAdmin')
            modalConsole = request.form.get('modalConsole')
            modalInput = request.form.get('modalInput')
            modalServers = request.form.get('modalServers')
            load_user(userEmail).admin = formToBool(modalAdmin)
            load_user(userEmail).viewConsole = formToBool(modalConsole)
            load_user(userEmail).typeInput = formToBool(modalInput)
            load_user(userEmail).createServer = formToBool(modalServers)
            modalDelete = request.form.get('modalDelete')
            if formToBool(modalDelete):
                db.session.delete(load_user(userEmail))
            db.session.commit()
            return redirect(url_for('views.admin'))

        return render_template('admin.html', user=current_user, userName=current_user.firstName, userlist=users)
    else:
        flash("Error! You are not an administrator and thus cannot access this page. Please contact one of the admins for assistance.", category="e")
        return render_template('failure.html', user=current_user, userName=current_user.firstName)
