from flask import Flask, render_template
from data import db_session
from data.termins import Term

app = Flask(__name__)
db_session.global_init('db/termins.db')
db_sess = db_session.create_session()
termins = db_sess.query(Term).all()



@app.route('/')
def a():
    return render_template('main_page.html', termins=termins)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)