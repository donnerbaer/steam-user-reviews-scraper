""" This script creates the database and the tables in the database.
"""

from app import database
import config

with open(config.SCHEMA_PATH, "r", encoding="utf-8") as f:
    db = database.Database()
    cursor = db.get_cursor()
    cursor.executescript(f.read())
    db.commit()
    db.close()
