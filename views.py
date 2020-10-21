from flask import Blueprint,render_template
from . import db
bp = Blueprint('main', __name__)
from flask_login import login_required

@bp.route('/')
@bp.route('/index')
@bp.route('/home')
@login_required
def index():
    return render_template('Home_Page.html')

@bp.route('/creation')
@login_required
def itemcreation():
    return render_template('Item Creation.html')

@bp.route('/detial')
@login_required
def watchdetialpage():
    return render_template('Watch detial page.html')

@bp.route('/list')
@login_required
def watchlist():
    return render_template('Watchlist.html')

@bp.route('/create_db')
def create_db():
    db.create_all()
    return "db create"

@bp.route("/drop_db")
def drop_db():
    db.drop_all()
    return "db drop"