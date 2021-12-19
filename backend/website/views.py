from flask import Blueprint

# this is where we put "routes" i.e. the pages our user can visit

# define that this is a blueprint
views = Blueprint('views', __name__)

#define a view/blueprint. @ symbol is called a 'decorator'
@views.route('/')
def home():
    return '<h1>Test</h1>'
