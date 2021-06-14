"""General page routes."""
from flask import Blueprint, request, render_template,flash, session ,redirect, url_for
from flask import current_app as app
from flask_mysqldb import MySQL

# Blueprint Configuration
signup_bp = Blueprint(
    "signup_bp", __name__, template_folder="templates", static_folder="static"
)

mysql = MySQL(app)

@signup_bp.route("/sign_up", methods=["GET","POST"])
def sign_up():
    """Sign Up Page."""

    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        mycursor = mysql.connection.cursor()
        mycursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        user = mycursor.fetchone()

        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            #DATABASE STUFF OCCURS
            # ADD New User Query

            data_user = (email ,password1 ,first_name)
            add_user = ("INSERT INTO user "
                        "(email,password,first_name) "
                        "VALUES (%s, %s, %s)")
            
            mycursor = mysql.connection.cursor()
            mycursor.execute(add_user, data_user)
            mysql.connection.commit()

            user_id = mycursor.lastrowid

            session['loggedin'] = True
            session['id'] = user_id
            session['email'] = email
            
            flash('Account created!', category='success')
            return redirect(url_for('home_bp.home'))

    return render_template(
        "signup_main.html",
        title="Flask Blueprint Demo",
        subtitle="Demonstration of Flask blueprints in action.",
        template="home-template"
    )