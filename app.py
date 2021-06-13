from flask import Flask, redirect, url_for, render_template
from dotenv import load_dotenv


app = Flask(__name__)

"""Application entry point."""
from spotify_application import init_app

app = init_app()

if __name__ == "__main__":
    app.run(debug=True)

# We can add a check early on that we continue to call Like below
'''
@app.before_request
def before_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None
'''
# This would make everything look cleaner like you had mentioned


