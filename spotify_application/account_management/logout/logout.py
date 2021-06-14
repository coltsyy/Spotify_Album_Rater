"""General page routes."""
from flask import Blueprint, redirect, url_for, session
from flask import current_app as app


# Blueprint Configuration
logout_bp = Blueprint(
    "logout_bp", __name__, template_folder="templates", static_folder="static"
)


@logout_bp.route('/logout')
def logout():

    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    
    return redirect(url_for('login_bp.login'))
