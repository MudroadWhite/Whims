from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from auth import login_required
from database import Database

bp = Blueprint('blog', __name__, url_prefix='/blog')  # ??

# TODO: blog & home difference
# TODO: database
@bp.route('/')
@login_required
def index():
    db = Database()
    posts = db.get_all_posts(g.user)
    print("Blog.index")
    return render_template('blog/index.html', posts=posts)

# TODO: to be updated
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = Database()
            db.create_post(title, body, g.user)
            db.close()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

# TODO: to be updated
@bp.route('/update', methods=('GET', 'POST'))
@login_required
def update():
    return render_template('blog/update.html')