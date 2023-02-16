
import sqlalchemy
from .db_session import SqlAlchemyBase


class Terms_Sposobin(SqlAlchemyBase):
    __tablename__ = 'terms_sposobin'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    definition = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    pictures_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    paragraph = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

class Terms_Vahromeev(SqlAlchemyBase):
    __tablename__ = 'terms_vahromeev'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    definition = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    pictures_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    paragraph = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)


class Terms_Alexeev(SqlAlchemyBase):
    __tablename__ = 'terms_alexeev'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    definition = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    pictures_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    paragraph = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
