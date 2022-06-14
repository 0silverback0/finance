from flask_wtf import FlaskForm
from wtforms import EmailField, RadioField, SelectField, StringField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    stock1 = StringField('stock 1', validators=[DataRequired()])
    stock2 = StringField('stock 2', validators=[DataRequired()])
    stock3 = StringField('stock 3', validators=[DataRequired()])
    stock4 = StringField('stock 4', validators=[DataRequired()])