# import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from database import Database

bp = Blueprint('home', __name__, url_prefix='/home')

# TODO: require login
# TODO: home functionalities

@bp.route('/', methods=('GET', 'POST'))
def homepage():
    # TODO: if logged in return homepage else return index
    return render_template("home/home.html")
    pass