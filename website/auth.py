# This file has everything to do with authentication 
from flask import Blueprint #This will help us define this file as a blueprint of the application (routes / URL's)

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up")
def sign_up():
    return "<p>Sign Up</p>"