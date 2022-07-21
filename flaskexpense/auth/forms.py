from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import Email, EqualTo, InputRequired, Length, ValidationError
from flask import flash


from flaskexpense.models import User


class Form_Manager(FlaskForm):

    username = StringField(
        "Username",
        [
            InputRequired(message="Enter the User-Name"), Length(min=3, max=20)
        ],
    )

    email = StringField("Email",
                        [
        InputRequired(message="Enter Email-Id"), Email()
    ])

    password = PasswordField(
        "Password", [
            InputRequired(message="Enter password"), Length(min=3, max=20),
        ]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        [
            InputRequired(message="Confirm Password"),
            EqualTo("password", message="Not some Passwords...must match"),
        ],
    )

    submit = SubmitField("Sign Up")


    def email_validator(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email by this Email already ExistF")


class LoginForm(FlaskForm):
    email = StringField("Email", [InputRequired(message="Enter Email"), Email()])
    password = PasswordField(
        "Password", [InputRequired(message="Enter Password")]
    )

    remember = BooleanField("Click me to Remember you")
    submit = SubmitField("Sign In")



def validate_category(self, field):
    if field.data == "":
        raise ValidationError("Select Category")
