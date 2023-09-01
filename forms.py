"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField

class AddPetform(FlaskForm):
    """Form for adding a pet to adoption database."""

    name = StringField("Pet Name")
    species = StringField("Pet Species")
    photo_url = TextAreaField("Photo URL")
    age = SelectField('Pet Age',
                      choices=[('baby', 'Baby'), ('young', 'Young'),
                               ('adult', 'Adult'), ('senior', 'Senior')])
    notes = TextAreaField("Any pet notes")
    available = BooleanField("Is available")