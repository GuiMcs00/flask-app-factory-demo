from flask import Blueprint

"""Create your blueprints routes here."""

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return 'Hello World!'
