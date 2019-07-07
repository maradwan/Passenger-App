# -*- coding: utf-8 -*-

from flask import Flask
from os import environ as env
from uuid import uuid4
import csv

# Init app
app = Flask(__name__)

import api.routes


app.config['SQLALCHEMY_DATABASE_URI'] = env.get("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env.get("SQLALCHEMY_TRACK_MODIFICATIONS")
app.secret_key = env.get("APP_SECRET_KEY")



from .models import Raw_data, db, raw_data_schema, raw_datas_schema


def load_data(filename):
        with open(filename) as f:
                reader = csv.reader(f)
                for row in reader:
                    uuid = uuid4()
                    new_raw_data = Raw_data(uuid,int(row[0]), int(row[1]), str(row[2]), str(row[3]), float(row[4]), int(row[5]), int(row[6]), float(row[7]))       
                    db.session.add(new_raw_data)
                    db.session.commit()

# Database
with app.app_context():
        db.init_app(app)
        db.create_all()  
        
# Load the data        
        try:
                load_data(env.get("FILENAME_CSV"))
        except Exception as e:
                print('Caught this error: ' + repr(e))

