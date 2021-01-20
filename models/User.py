from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincremnet=True)
    login = db.Column(db.String(250), nullable=False)

    def __init__(self, login):
        self.login = login
