"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField

from wtforms.validators import InputRequired, URL, AnyOf, Optional


class AddPetform(FlaskForm):
    """Form for adding a pet to adoption database."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Pet Species", validators=[
                          InputRequired(), AnyOf(values=['porcupine', 'dog', 'cat'])])
    photo_url = TextAreaField("Photo URL", validators=[Optional(), URL()])
    age = SelectField('Pet Age',
                      choices=[('baby', 'Baby'), ('young', 'Young'),
                               ('adult', 'Adult'), ('senior', 'Senior')], validators=[InputRequired(), AnyOf(values=['baby', 'young', 'adult', 'senior'])])
    notes = TextAreaField("Any pet notes", validators=[Optional()])
    available = BooleanField("Is available", default=True)
