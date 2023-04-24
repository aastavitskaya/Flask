from sqlalchemy import Column, Integer, String, Boolean
from blog.models.database import db
from flask_login import UserMixin
from blog.security import flask_bcrypt

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255))

    def __repr__(self):
        return f"<User #{self.id} {self.email!r}>"
    
    # @property
    # def password(self):
    #     return self._password

    # @password.setter
    # def password(self, value):
    #     self._password = flask_bcrypt.generate_password_hash(value)

    # def validate_password(self, password) -> bool:
    #     return flask_bcrypt.check_password_hash(self._password, password)