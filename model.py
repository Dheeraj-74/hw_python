from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    address = db.Column(db.String(200))
    phone_number = db.Column(db.String(20), nullable = False)

    def __repr__(self):
        return f"<Contact {self.name}>"