from . import db
from flask_login import UserMixin

# maybe add a logs table?

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    admin = db.Column(db.Boolean, default=False)
    viewConsole = db.Column(db.Boolean, default=False)
    typeInput = db.Column(db.Boolean, default=False)
    createServer = db.Column(db.Boolean, default=False)