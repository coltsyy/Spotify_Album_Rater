"""General page routes."""
from flask import Blueprint
from flask import current_app as app
from flask import render_template

# Blueprint Configuration
profile_bp = Blueprint(
    "profile_bp", __name__, template_folder="templates", static_folder="static"
)


@profile_bp.route("/profile", methods=["GET"])
def main():
    """Profile."""
    return render_template(
        "profile_main.html",
        title="Flask Blueprint Demo",
        subtitle="Demonstration of Flask blueprints in action.",
        template="home-template"
    )