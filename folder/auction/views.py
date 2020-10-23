from flask import Blueprint,render_template
from . import db
bp = Blueprint('main', __name__)
from flask_login import login_required,current_user

@bp.route('/')
@bp.route('/index')
@bp.route('/home')
def index():
    username=''
    try:
        username=current_user.username
    except Exception as e:
        print(e)
        pass
    return render_template('Home_Page.html',title='HomePage-watch auction store',username=username)

@bp.route('/creation')
@login_required
def itemcreation():
    return render_template('Item Creation.html',title='Watch detial page')

@bp.route('/detial')
@login_required
def watchdetialpage():
    return render_template('Watch detial page.html',title='Watch detail page')

@bp.route('/list')
@login_required
def watchlist():
    return render_template('Watchlist.html',title='Wantchlist')

@bp.route('/create_db')
def create_db():
    db.create_all()
    return "db create"

@bp.route("/drop_db")
def drop_db():
    db.drop_all()
    return "db drop"