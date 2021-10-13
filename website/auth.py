# This file has everything to do with authentication 
from flask import Blueprint, render_template, request, flash    #This will help us import the necesary library for this file to be a blueprint (Blueprint) of
                                                                # the application (routes / URL's), the library to render the templates(render_template),
                                                                # the library to get the information sent by forms (request), and the library to flash messages (flash)

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])  #Within the methods, by default you can 'GET', but now (because it has been specified) you can also 'POST;
def login():
    return render_template("login.html", boolean=True)                 #The second argument "text" will be a usable variable in the login.html
                                                                        #template, you can call it by using {{variable_name}}

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
            pass
        elif len(firstName) < 2:
            flash('Email must be greater than 1 character.', category='error')
            pass
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
            pass
        elif len(password1) < 7:
            flash('Password must be at least 7', category='error')
            pass
        else:
            flash('Account created!', category='succes')
            # add user to the database 

    return render_template("sign_up.html")