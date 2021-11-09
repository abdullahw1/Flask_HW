from myapp import myapp_obj
from flask import render_template, url_for, flash, redirect
from myapp.forms import TopCities
from flask import render_template, flash, redirect

from myapp import db
from myapp.models import Cities
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route("/login", methods=['GET', 'POST'])
def home():
    title = 'Top Cities'
    form = TopCities()
    name = 'Abdullah'
    if form.validate_on_submit():
        city = Cities(city_name = form.city_name.data, city_rank = form.city_rank.data, is_visited = form.is_visited.data)
        db.session.add(city)
        db.session.commit()
        flash(f'{form.city_name.data} submitted!')
        return redirect('/')

    top_cities = Cities.query.order_by(Cities.city_rank).all()
    return render_template('home.html', form = form, title = title, name=name, top_cities=top_cities)
