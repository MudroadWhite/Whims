from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from auth import login_required
from database import Database

bp = Blueprint('blog', __name__, url_prefix='/blog')  # ??

# TODO: Add entries to database & `posts` variable:
#  - author id
#  - time
#  - (future) likes? reposts? comments?

@bp.route('/')
@login_required
def index():
    db = Database()
    posts = db.get_all_posts(g.user)
    return render_template('blog/index.html', posts=posts)

# TODO: to be updated
@bp.route('/create', methods=('GET', 'POST'))
@login_required
# index.html
#
# { % if g.user['id'] == post['author_id'] %}<a class ="action" href="{{ url_for('blog.update', id=post['id']) }}" > Edit < /a >{ % endif %}
#
#           <h1>{{ post['title'] }}</h1>
#           <div class="about">by {{ post['username'] }} on {{ post['created'].strftime('%Y-%m-%d') }}</div>
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
            db.update_post(title, body, g.user)
            db.close()
            return redirect(url_for('blog.index'))
    return render_template('blog/update.html')