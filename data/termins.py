
import sqlalchemy
from .db_session import SqlAlchemyBase


class Term(SqlAlchemyBase):
    __tablename__ = 'terms'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    definition = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    pictures_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    music_id = sqlalchemy.Column(sqlalchemy.Integer, index=True, unique=True, nullable=True)
    paragraph = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
