"""General page routes."""
from flask import Blueprint
from flask import current_app as app
from flask import render_template

# Blueprint Configuration
friends_ratings_bp = Blueprint(
    "friends_ratings_bp", __name__, template_folder="templates", static_folder="static"
)


@friends_ratings_bp.route("/friends_ratings", methods=["GET"])
def main():
    """Your Ratings."""
    return render_template(
        "friends_ratings_main.html",
        title="Flask Blueprint Demo",
        subtitle="Demonstration of Flask blueprints in action.",
        template="home-template"
    )