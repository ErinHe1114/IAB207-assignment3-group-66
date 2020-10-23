from flask_sqlalchemy import SQLAlchemy

from . import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(16),nullable=False)
    password = db.Column(db.String(16),nullable=False)
    email = db.Column(db.String(16),nullable=False)
    is_active=db.Column(db.Boolean,default=True)
    is_authenticated=db.Column(db.Boolean,default=True)
    is_anonymous=db.Column(db.Boolean,default=True)
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email
    def get_id(self):
        return self.id