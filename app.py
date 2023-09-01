"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetform, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def get_homepage():
    """Loads homepage."""

    pets = Pet.query.all()

    return render_template('homepage.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add pet form; handle adding."""

    form = AddPetform()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data.lower()
        photo_url = form.photo_url.data or None
        age = form.age.data
        notes = form.notes.data or None
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url,
                      age=age, notes=notes, available=available)

        db.session.add(pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template("add_pet_form.html", form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet_details(pet_id):
    """Get pet details page, and handle form submission for editing pet details."""

    pet = Pet.query.get_or_404(pet_id)
    form =EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data or None
        pet.notes = form.notes.data or None
        pet.available = form.available.data

        db.session.commit()

        return redirect(f'/{pet_id}')
    else:
        return render_template('pet_details.html', form=form, pet=pet)