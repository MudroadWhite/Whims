from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from auth import login_required
from database import Database

bp = Blueprint('contact', __name__, url_prefix='/contact')  # ??
@bp.route('/')
@login_required
def index():
    db = Database()
    contacts = db.get_all_contacts(g.user)
    for i in range(len(contacts)):
        # TODO: future: optimize this sentence into SQL
        contacts[i]['username'] = db.get_name_from_id(contacts[i]['user2_id'])
    db.close()
    return render_template('contact/index.html', contacts=contacts)

# TODO: (IMPORTANT) implement chat functionality
@bp.route('/chat', methods=('GET', 'POST'))
def chat(uid1, uid2):
    db = Database()
    u1 = db.get_name_from_id(uid1)
    u2 = db.get_name_from_id(uid2)
    db.close()
    print([u1, u2])
    return render_template('contact/chat.html')