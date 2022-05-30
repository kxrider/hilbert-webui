from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager
from flask_mail import Mail, Message

db = SQLAlchemy()
mail = Mail()
DB_NAME = 'database.db' #test change

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aoiejwg oaiewg'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'hilbert.host@gmail.com'
    app.config['MAIL_PASSWORD'] = 'kP3C&f3FRYhf&ehYu'
    #app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_DEFAULT_SENDER'] = 'hilbert.host@gmail.com'
    app.config['MAIL_DEBUG'] = True
    app.config['MAIL_SUPPRESS_SEND'] = False
    db.init_app(app)
    mail.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User # so that code in models is called
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #where to go if we're not logged in, and login required?
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    print(DB_NAME)
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
