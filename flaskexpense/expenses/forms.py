from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, SelectField, StringField, SubmitField
from wtforms.validators import InputRequired, Length, NumberRange, ValidationError
from wtforms.fields.html5 import DateField as Date

categories = [
    ("", "choose from list"),
    ("Shopping", "Shopping"),
    ("Travel", "Travel"),
    ("Food", "Food"),
    ("Gifts", "Gifts"),
    ("Electronics", "Electronics"),
    ("Book", "Book"),
    ("CarParking", "carParking"),
    ("Parties", "Parties"),
    ("Education", "Education"),
    ("Medical", "Medical"),
    ("Transportation", "Transportation"),
    ("Clothes", "Clothes"),
    ("Rent", "Rent"),
    ("Other", "Other"),
]


def validate_category(self, field):
    if field.data == "":
        raise ValidationError("Select category of Expense")


class ExpenseForm(FlaskForm):
    name = StringField("Name", [InputRequired(message="Enter your Expense Name"), Length(max=50)])

    date = Date("Date")

    category = SelectField("Category", choices=categories, validators=[validate_category])

    price = FloatField(
        "Amount",
        [
            InputRequired(message="Enter Expense Sum"),
            NumberRange(min=0, message="Amount should be positive"),
        ],
    )
    submit = SubmitField("Submit")


class DateForm(FlaskForm):
    start_date = Date("Start Date")
    end_date = Date("End Date")
    submit = SubmitField("Show")

    def correct_end_date(self, end_date):
        if end_date.data < self.start_date.data:
            raise ValidationError("End date must not be earlier than start date.")
