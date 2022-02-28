from flask import Flask, render_template
from flask.ext.heroku import Heroku
from data import db_session
from data.termins import Term

app = Flask(__name__)
db_session.global_init('db/termins.db')
db_sess = db_session.create_session()
termins = db_sess.query(Term).all()
heroku = Heroku()


@app.route('/')
def a():
    return render_template('main_page.html', termins=termins)

heroku.init_app(app)