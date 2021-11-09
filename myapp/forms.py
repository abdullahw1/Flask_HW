from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TopCities(FlaskForm):
    city_name = StringField('City Name',validators=[DataRequired(), Length(min=3, max=30)])
    city_rank = IntegerField('City Rank', validators=[DataRequired()])
    is_visited = BooleanField('Visited')
    submit = SubmitField('Submit')

