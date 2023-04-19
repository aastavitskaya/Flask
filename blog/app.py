from flask import Flask, render_template
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db
from blog.views.auth import login_manager, auth_app
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix='/auth')

config_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.config.{config_name}")

db.init_app(app)
login_manager.init_app(app)

@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")

@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User
    admin = User(username="admin", is_staff=True)
    james = User(username="james")

    db.session.add(admin)
    db.session.add(james)
    db.session.commit()

    print("done! created users:", admin, james)

@app.route("/")
def index():
    return render_template("index.html")