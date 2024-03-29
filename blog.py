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

# TODO: (IMPORTANT)
#   - Change blog template from text to buttons or DAW design
#   - Add date functionality

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
        # TODO: add date time
        date = None
        time = None
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = Database()
            # TODO: add date time
            db.create_post(title, body, g.user)
            db.close()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

# TODO:
#  [x] Handle author_id issue when rendering template
#  [ ] (Future) Move most logic into frontend side in the future
@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):

    db = Database()
    post = db.get_post(id)
    db.close()

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
            db.update_post(title, body, id)
            db.close()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST','GET'))
@login_required
def delete(id):
    db = Database()
    post = db.get_post(id)
    if post != [] and post:  # Check if post exists
        db.delete_post(id)
    db.close()
    return redirect(url_for('blog.index'))