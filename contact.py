from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from auth import login_required
from database import Database

bp = Blueprint('blog', __name__, url_prefix='/contact')  # ??

@bp.route('/')
@login_required
def index():
    db = Database()
    # TODO: get all contacts
    # TODO: design contact table / user add contact entry
    contacts = None
    return render_template('contact/index.html', contacts=contacts)