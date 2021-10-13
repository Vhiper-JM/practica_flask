# Here, the standard routes for our website (where users can actually go to) will be stored 
from flask import Blueprint, render_template #This will help us define this file as a blueprint of the application (routes / URL's), and render the templates

views = Blueprint('views', __name__)    #This is how you will define the Blueprint

@views.route('/')
def home():    #This function will run whenever you go to '/URL'
    return render_template("home.html")

