from datetime import timezone
from website import db  #The database from __init__ is imported
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):   #Logic for the notes in the website (it's main purpose)
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))    #This user_id will be directly related to id integer attribute from the class User
     

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)  #unique=True makes it so that no two users can have the same email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
