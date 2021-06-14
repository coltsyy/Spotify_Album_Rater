"""General page routes."""
from flask import Blueprint ,render_template,request, flash, redirect, url_for,session, jsonify
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask_mysqldb import MySQL
import json
import ast

mysql = MySQL(app)

# Blueprint Configuration
login_bp = Blueprint(
    "login_bp", __name__, template_folder="templates", static_folder="static"
)


@login_bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'POST':
        
        email = request.form.get('email')
        password = request.form.get('password')
        
        mycursor = mysql.connection.cursor()
        mycursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password,))

        account = mycursor.fetchone()

        print(account)

        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[0]
            session['email'] = email
            # Redirect to home page
            flash('Logged in successfully!', category='success')
            return redirect(url_for('home_bp.home') )
        else:
            flash('Incorrect email or password, try again.', category='error')
            return redirect(url_for('login_bp.login') )



    return render_template(
        "login_main.html",
        title="Flask Blueprint Demo",
        subtitle="Demonstration of Flask blueprints in action.",
        template="home-template"
    )