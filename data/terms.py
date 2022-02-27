import sqlite3
from data.termins import Term
from data import db_session
db_session.global_init("db/termins.db")

con = sqlite3.connect('C:/Users/danil/PycharmProjects/db/termins.db')
cur = con.cursor()
result = cur.execute("""select * from terms""").fetchall()
for i in result:
    term = Term()
    term.name = i[1]
    term.definition = i[2]
    term.pictures_id = i[3]
    term.music_id = i[4]
    term.paragraph = i[5]
    db_sess = db_session.create_session()
    db_sess.add(term)
    db_sess.commit()
con = sqlite3.connect('C:/Users/danil/PycharmProjects/db/termins.db')
cur = con.cursor()

result = cur.execute("""select * from pictures""").fetchall()
for i in result:
    picture = Pictures()
    picture.picture_path = i[1]
    db_sess = db_session.create_session()
    db_sess.add(picture)
    db_sess.commit()

con = sqlite3.connect('C:/Users/danil/PycharmProjects/db/termins.db')
cur = con.cursor()

result = cur.execute("""select * from music""").fetchall()
for i in result:
    picture = Music()
    picture.music_path = i[1]
    db_sess = db_session.create_session()
    db_sess.add(picture)
    db_sess.commit()
