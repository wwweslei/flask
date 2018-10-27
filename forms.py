from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class FormPassword(FlaskForm):
    site = StringField('Site', validators=[DataRequired()])
    username = StringField('User Name')
    email = StringField('Email')
    password = StringField('Passaword', validators=[DataRequired()])
    submit = SubmitField('submit')
