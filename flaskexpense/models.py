from flask_login import UserMixin
from flaskexpense import db, login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    expenses = db.relationship("Expense", backref="user", lazy=True)

    def __repr__(self):  # string representation of an object
        return f"User('{self.username}', '{self.email}')"


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(20), nullable=False)

    def __repr__(self):  # string representation of an object
        return (
            f"Expense('{self.name}', '{self.category}', '{self.price}', '{self.date}')"
        )
