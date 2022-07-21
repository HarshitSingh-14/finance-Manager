import click
from os import path
from flask import Flask
from flask_bcrypt import Bcrypt
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_Name = "data.db"


bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "myusers.login"


def create_app():


    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'huehue'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_Name}'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from flaskexpense.main.routes import main
    app.register_blueprint(main)
    from flaskexpense.auth.routes import myusers
    app.register_blueprint(myusers)
    from flaskexpense.expenses.routes import expenses
    app.register_blueprint(expenses)
    from flaskexpense.plots.routes import plots
    app.register_blueprint(plots)
    from flaskexpense.errors.handlers import errorPages
    app.register_blueprint(errorPages)

    from .models import User, Expense



    @click.command("create_tables")
    @with_appcontext

    def create_tables():
        if not path.exists('./'+ DB_Name):
            db.create_all()
            print("database is created....")
    app.cli.add_command(create_tables)

    return app
