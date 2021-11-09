from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TopCities(FlaskForm):
    cityName = StringField('City Name',validators=[DataRequired(), Length(min=3, max=30)])
    cityRank = IntegerField('City Rank', validators=[DataRequired()])
    isVisited = BooleanField('Visited')
    submit = SubmitField('Submit')

