from app import db
from datetime import datetime


class Password(db.Model):
    __tablename__ = "passwords"
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(20), unique=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(20))
    password = db.Column(db.String(100))
    date = db.Column(db.DateTime)

    def __init__(self, site, username, email, password):
        self.site = site
        if username:
            self.username = username
        else:
            self.username = "wwweslei"
        if email:
            self.email = email
        else:
            self.email = "www.weslei@gmail.com"
        self.password = password
        self.date = datetime.utcnow()

    def __repr__(self):
        return '<DB Site %r>' % self.site

    def __getitem__(self, position):
        self.lista = [self.site, self.username, self.email,
                      self.password, self.date]
        return self.lista[position]
db.create_all()