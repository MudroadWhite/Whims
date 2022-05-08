# import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from database import Database

from auth import login_required

# TODO: home to be prefixed with username
bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('/')
@login_required
def homepage():
    if g.user is None or g.username is None:
        session.clear()
        flash("Login required")  # ??
        return redirect(url_for('index'))
    else:
        return render_template("home/home.html")

# For viewing other user's homepage
# Public to the internet
@bp.route('/view')
def view(uid):
    # TODO: get user id, render into the view template
    return render_template("home/view.html")