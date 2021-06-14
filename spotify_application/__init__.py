"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment


def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .home import home
        from .profile import profile

        from .ratings.your_ratings import your_ratings
        from .ratings.friends_ratings import friends_ratings

        from .account_management.signup import signup
        from .account_management.login import login
        from .account_management.logout import logout
    


        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(profile.profile_bp)
        
        app.register_blueprint(your_ratings.your_ratings_bp)
        app.register_blueprint(friends_ratings.friends_ratings_bp)

        app.register_blueprint(signup.signup_bp)
        app.register_blueprint(login.login_bp)
        app.register_blueprint(logout.logout_bp)
        



        return app