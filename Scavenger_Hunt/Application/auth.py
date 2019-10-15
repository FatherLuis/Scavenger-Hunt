from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


bp = Blueprint('auth', __name__)

@bp.route('/register',methods=('GET', 'POST'))
def register():
    # CHECK IF USER IS FOUND IN THE DATABASE.
    return render_template('auth/register.html')

@bp.route('/login',methods=('GET', 'POST'))
def login():
    # CHECK CREDENTIALS
    return render_template('auth/login.html')