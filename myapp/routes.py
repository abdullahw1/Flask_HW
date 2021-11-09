from myapp import myapp_obj
from flask import render_template, url_for, flash, redirect
from myapp.forms import TopCities
from flask import render_template, flash, redirect

from myapp import db
from myapp.models import Cities
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route("/login", methods=['GET', 'POST'])
def home():
    form = TopCities()
    title = 'Top Cities'
    name = 'Abdullah'
    top_cities = User.query.all()
    if form.validate_on_submit():
        city = Cities(cityName = form.cityName.data, cityRank = form.cityRank.data, isVisited = form.isVisited.data)
        db.session.add(city)
        db.session.commit()
        return redirect('/')

    top_cities = City.query.order_by(City.city_rank).all()
    return render_template('home.html', form = form, title = title, name=name, top_cities=top_cities)
