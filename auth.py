import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from database import Database

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
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
            print("Checking username {u}".format(u=username))
            print(db.check_user_exists(username))
            if not db.check_user_exists(username):
                db.register_user(username, password)
                db.close()
                return redirect(url_for("auth.login"))
            else:
                error = f"User {username} is already registered."
            db.close()

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']
    #     error = None
    #
    #     if not username:
    #         error = 'Username is required.'
    #     elif not password:
    #         error = 'Password is required.'
    #
    #     if error is None:
    #         db = Database()
    #         print("Checking username {u}".format(u=username))
    #         print(db.check_user_exists(username))
    #         if not db.check_user_exists(username):
    #             db.register_user(username, password)
    #             db.close()
    #             return redirect(url_for("auth.login"))
    #         else:
    #             error = f"User {username} is already registered."
    #         db.close()
    #
    #     flash(error)
    # return render_template('auth/register.html')
    pass