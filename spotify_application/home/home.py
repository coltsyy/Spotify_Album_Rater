"""General page routes."""
from flask import Blueprint, session, redirect, url_for
from flask import current_app as app
from flask import render_template


# Blueprint Configuration
home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route("/", methods=["GET"])
def home():
    """Homepage."""

    if 'id' not in session:
        return redirect(url_for('login_bp.login'))

    else:
        return render_template(
            "index.html",
            title="Flask Blueprint Demo",
            subtitle="Demonstration of Flask blueprints in action.",
            template="home-template"
        )

