from flask import g
import sqlite3
from os.path import abspath, dirname


def connect_db():
    db_file_name = dirname(abspath(__file__)) + '\\members.db'
    #  print(db_file_name)
    db = sqlite3.connect(db_file_name)
    db.row_factory = sqlite3.Row
    return db


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db