from flask import Blueprint

view = Blueprint("views", __name__)


@view.route('/')
def home():
    return "Hello there"

