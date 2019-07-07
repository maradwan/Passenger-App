from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import text as sa_text


app = Flask(__name__)

# Init db
db = SQLAlchemy()
# Init ma
ma = Marshmallow(app)


# Data Class/Model
class Raw_data(db.Model):
  uuid = db.Column(db.String(200), primary_key=True)
  survived = db.Column(db.Boolean)
  passengerClass = db.Column(db.Integer)
  name = db.Column(db.String(200))
  sex = db.Column(db.String(200))
  age = db.Column(db.Float)
  siblingsOrSpousesAboard = db.Column(db.Integer)
  parentsOrChildrenAboard = db.Column(db.Integer)
  fare = db.Column(db.Float)


  def __init__(self, uuid, survived, passengerClass, name, sex, age, siblingsOrSpousesAboard, parentsOrChildrenAboard, fare):
    self.uuid = uuid
    self.survived = survived
    self.passengerClass = passengerClass 
    self.name = name  
    self.sex = sex 
    self.age = age 
    self.siblingsOrSpousesAboard = siblingsOrSpousesAboard
    self.parentsOrChildrenAboard = parentsOrChildrenAboard 
    self.fare = fare
 

# raw_data Schema
class RawdataSchema(ma.Schema):
    class Meta:
        fields = ('uuid', 'survived', 'passengerClass', 'name', 'sex', 'age', 'siblingsOrSpousesAboard', 'parentsOrChildrenAboard', 'fare')

# Init schema
raw_data_schema = RawdataSchema(strict=True)
raw_datas_schema = RawdataSchema(many=True, strict=True)