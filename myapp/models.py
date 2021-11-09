from myapp import db

class City(UserMixin, db.Model):
from city import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cityName = db.Column(db.String(30), index=True)
    cityRank = db.Column(db.Integer())
    isVisited = db.Column(db.Boolean)

    def __repr__(self):
        return f"City('{self.city_name}', {self.city_rank}, {self.is_visited})"
