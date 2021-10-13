# Here, the standard routes for our website (where users can actually go to) will be stored 
from flask import Blueprint, render_template, request, flash, jsonify #This will help us define this file as a blueprint of the application (routes / URL's), and render the templates
from flask_login import login_required, current_user  # the current_user method will detect whether a user is loged in or not
from .models import Note
from website import db
import json

views = Blueprint('views', __name__)    #This is how you will define the Blueprint

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():    #This function will run whenever you go to '/URL'
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})

