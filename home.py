# import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from database import Database

from auth import login_required

bp = Blueprint('home', __name__, url_prefix='/home')

# TODO: require login
# TODO: home functionalities

@bp.route('/', methods=('GET', 'POST'))
@login_required
def homepage():
    # TODO: if logged in return homepage else return index
    # return render_template("home/home.html")
    if g.user is None:
        return render_template("index.html")
    else:
        return redirect(url_for('blog.index'))
    pass