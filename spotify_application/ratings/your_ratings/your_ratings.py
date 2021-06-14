"""General page routes."""
from flask import Blueprint
from flask import current_app as app
from flask import render_template

# Blueprint Configuration
your_ratings_bp = Blueprint(
    "your_ratings_bp", __name__, template_folder="templates", static_folder="static"
)


@your_ratings_bp.route("/your_ratings", methods=["GET"])
def main():
    """Your Ratings."""
    return render_template(
        "your_ratings_main.html",
        title="Flask Blueprint Demo",
        subtitle="Demonstration of Flask blueprints in action.",
        template="home-template"
    )