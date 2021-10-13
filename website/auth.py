# This file has everything to do with authentication 
from flask import Blueprint, render_template #This will help us define this file as a blueprint of the application (routes / URL's), and render the templates

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")                  #The second argument "text" will be a usable variable in the login.html
                                                                        #template, you can call it by using {{variable_name}}

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")