import os
from flask.ext.heroku import Heroku
from flask import Flask, render_template, request
from data import db_session
from data.termins import Terms_Vahromeev, Terms_Sposobin, Terms_Alexeev
heroku = Heroku()
app = Flask(__name__)
db_session.global_init('db/termins.db')
db_sess = db_session.create_session()
termins_sposobin = db_sess.query(Terms_Sposobin).all()
termins_vahromeev = db_sess.query(Terms_Vahromeev).all()
termins_alexeev = db_sess.query(Terms_Alexeev).all()
union = [termins_sposobin, termins_vahromeev]


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        search = request.values.get('search_all', default='')
        termins_sposobin_searched = db_sess.query(Terms_Sposobin).filter(Terms_Sposobin.name.like(f'%{search}%'))
        termins_vahromeev_searched = db_sess.query(Terms_Vahromeev).filter(Terms_Vahromeev.name.like(f'%{search}%'))
        termins_alexeev_searched = db_sess.query(Terms_Alexeev).filter(Terms_Alexeev.name.like(f'%{search}%'))
        union_searched = [termins_sposobin_searched, termins_vahromeev_searched, termins_alexeev_searched]
        for e in union_searched:
            for i in e:
                print(i.name, i.id)
        print(search)
    return render_template('main_page.html', union=union_searched)


@app.route('/sposobin', methods=['GET', 'POST'])
def sposobin():
    search = request.values.get('search_s', default='')
    termins_sposobin_searched = db_sess.query(Terms_Sposobin).filter(Terms_Sposobin.name.like(f'%{search}%'))
    for e in termins_sposobin_searched:
        print(e.name)
    return render_template('sposobin.html', termins_s=termins_sposobin_searched)


@app.route('/vahromeev', methods=['GET', 'POST'])
def vahromeev():
    search = request.values.get('search_v', default='')
    termins_vahromeev_searched = db_sess.query(Terms_Vahromeev).filter(Terms_Vahromeev.name.like(f'%{search}%'))
    return render_template('vahromeev.html', termins_v=termins_vahromeev_searched)


@app.route('/alexeev', methods=['GET', 'POST'])
def alexeev():
    search = request.values.get('search_a', default='')
    termins_alexeev_searched = db_sess.query(Terms_Alexeev).filter(Terms_Alexeev.name.like(f'%{search}%'))
    return render_template('alexeev.html', termins_a=termins_alexeev_searched)



heroku.init_app(app)