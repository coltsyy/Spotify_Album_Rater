from flask import Flask, redirect, url_for, render_template
from dotenv import load_dotenv

app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template("index.html")

@app.route('login')
def login():
    return render_template("login.html")

@app.route('your_ratings')
def your_ratings():
    return render_template("your_ratings.html")

@app.route('friends_ratings')
def friends_ratings():
    return render_template("friends_ratings.html")
    
@app.route('settings')
def settings():
    return render_template("settings.html")


if __name__ == "__main__":
    app.run(debug=True)

