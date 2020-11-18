from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
import sqlalchemy.interfaces


class DontBeSilly(sqlalchemy.interfaces.PoolListener):
    def connect(self, dbapi_con, connection_record):
        cur = dbapi_con.cursor()
        cur.execute("SET SESSION sql_mode='TRADITIONAL'")
        cur = None

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mealplanner.db'
db = SQLAlchemy(app)
engine = create_engine('sqlite:///mealplanner.db?check_same_thread=False', listeners=[DontBeSilly()])
Session = sessionmaker(bind=engine)
session = Session()

from app import routes