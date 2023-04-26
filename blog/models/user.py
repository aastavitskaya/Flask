from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from blog.models.database import db
from flask_login import UserMixin
from blog.security import flask_bcrypt
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(String(255), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True)
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)
    _password = db.Column(LargeBinary, nullable=True)

    author = relationship("Author", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"
    
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self._password, password)