from flask import Flask, render_template_string, request
from flask_sqlalchemy import SQLAlchemy
from docassemble_flask_user import current_user, login_required, UserManager, UserMixin, SQLAlchemyAdapter

# Use a Class-based config to avoid needing a 2nd file
class ConfigClass(object):
    # Configure Flask
    SECRET_KEY = 'THIS IS AN INSECURE SECRET'                 # Change this for production!!!
    SQLALCHEMY_DATABASE_URI = 'sqlite:///minimal_app.sqlite'  # Use Sqlite file db
    CSRF_ENABLED = True

    # Configure Flask-User
    USER_ENABLE_EMAIL = False                   # Disable emails for now

# Setup Flask and read config from ConfigClass defined above
app = Flask(__name__)
app.config.from_object(__name__+'.ConfigClass')

# Initialize Flask extensions
db = SQLAlchemy(app)                            # Initialize Flask-SQLAlchemy

# Define User model. Make sure to add flask_user UserMixin!!
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, default='')
    active = db.Column(db.Boolean(), nullable=False, default=False)

# Create all database tables
db.create_all()

# Setup Flask-User
db_adapter = SQLAlchemyAdapter(db,  User)       # Select database adapter
user_manager = UserManager(db_adapter, app)     # Init Flask-User and bind to app

# The Home page is accessible to anyone
@app.route('/')
def home_page():
    if current_user.is_authenticated():
        return profile_page()
    return render_template_string("""
        {% extends "base.html" %}
        {% block content %}
        <h2>{%trans%}Home Page{%endtrans%}</h2>
        <p> <a href="{{ url_for('user.login') }}">{%trans%}Sign in{%endtrans%}</a> or
            <a href="{{ url_for('user.register') }}">{%trans%}Register{%endtrans%}</a></p>
        {% endblock %}
        """)

# The Profile page requires a logged-in user
@app.route('/profile')
@login_required                                 # Use of @login_required decorator
def profile_page():
    return render_template_string("""
        {% extends "base.html" %}
        {% block content %}
            <h2>{%trans%}Profile Page{%endtrans%}</h2>
            <p> {%trans%}Hello{%endtrans%}
                {{ current_user.username or current_user.email }},</p>
            <p> <a href="{{ url_for('user.change_username') }}">
                {%trans%}Change username{%endtrans%}</a></p>
            <p> <a href="{{ url_for('user.change_password') }}">
                {%trans%}Change password{%endtrans%}</a></p>
            <p> <a href="{{ url_for('user.logout') }}?next={{ url_for('user.login') }}">
                {%trans%}Sign out{%endtrans%}</a></p>
        {% endblock %}
        """)

# Start development web server
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

