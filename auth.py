import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from database import Database

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():  # ok
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            db = Database()
            if not db.check_user_exists(username):
                db.register_user(username, password)
                db.close()
                flash("Register successful")
                return redirect(url_for("auth.login"))
            else:
                error = f"User {username} is already registered."
            db.close()

        if error is not None:
            flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            db = Database()
            if db.login(username, password):
                session.clear()
                session['user_id'] = db.get_user_id_from_name(username)  # user['id']
                session['username'] = username
                return redirect(url_for("home.homepage"))
            else:
                error = "Login failed. Check your username or password."
            db.close()
        if error is not None:
            flash(error)
    return render_template('auth/login.html')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            error = "Required Login"
            flash(error)
            print("g,user is None")
            return redirect(url_for('auth.login'))
        return view(**kwargs)

    return wrapped_view

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    username = session.get('username')
    if user_id is None:
        g.user = None
        g.username = None
    else:
        g.user = user_id
        g.username = username

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
