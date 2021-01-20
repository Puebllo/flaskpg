from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import User

db = SQLAlchemy()
app = Flask(__name__)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskpgdb.sqlite3'

    db.init_app(app)

    return app



if __name__ == '__main__':
    #app.run()
    create_app()


@app.route('/')
def hello():
    user = User("pueblo")
    return f"Hello {user.login} !"