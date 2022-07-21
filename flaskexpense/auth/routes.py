from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash , check_password_hash
from flaskexpense import bcrypt, db
from flaskexpense.auth.forms import LoginForm, Form_Manager
from flaskexpense.models import User

myusers = Blueprint("myusers", __name__)


@myusers.route("/signup", methods=["GET", "POST"])
def signup():

    if current_user.is_authenticated:
        return redirect(url_for("expenses.dashboard"))
    form = Form_Manager()

    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )

        newuser = User(username=form.username.data, email=form.email.data, password=hash_password)
        # db.create_all()
        db.session.add(newuser)
        db.session.commit()

        return redirect(url_for("myusers.login"))
    return render_template("auth/signup.html", form=form)


@myusers.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("expenses.dashboard"))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return (
                redirect(next_page)
                if next_page
                else redirect(url_for("expenses.dashboard"))
            )
    return render_template("auth/login.html", form=form)


@myusers.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@myusers.route("/aboutMe")
@login_required
def aboutMe():
    return render_template("dashboard/aboutMe.html")
