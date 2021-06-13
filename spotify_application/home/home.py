"""General page routes."""
from flask import Blueprint
from flask import current_app as app
from flask import render_template


# Blueprint Configuration
home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route("/", methods=["GET"])
def home():
    """Homepage."""
    return render_template(
        "index.html",
        title="Flask Blueprint Demo",
        subtitle="Demonstration of Flask blueprints in action.",
        template="home-template"
    )


@home_bp.route("/login", methods=["GET"])
def login():
    """login."""
    return render_template(
        "login.html",
        title="Flask Blueprint Demo",
        subtitle="Demonstration of Flask blueprints in action.",
        template="home-template"
    )