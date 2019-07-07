from flask import Flask, request, jsonify, render_template
from uuid import uuid4
from .models import Raw_data, db, raw_data_schema, raw_datas_schema
from .swagger import SWAGGER_URL, API_URL, SWAGGERUI_BLUEPRINT
from api import app
from os import environ as env
from uuid import uuid4


### swagger specific ###
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

## UI 
@app.route('/showall')
def showall():
   return render_template('showall.html', passengers = Raw_data.query.all())

@app.route('/')
def home():
  return render_template('home.html')
   

# Create a Data
@app.route('/people', methods=['POST'])
def add_data():
    uuid = uuid4()
    try:
        survived = request.json['survived']
        passengerClass = int(request.json['passengerClass'])
        name = request.json['name']
        sex = request.json['sex']
        age = request.json['age']
        siblingsOrSpousesAboard = request.json['siblingsOrSpousesAboard']
        parentsOrChildrenAboard = request.json['parentsOrChildrenAboard']
        fare = request.json['fare']

        new_raw_data = Raw_data(uuid, survived, passengerClass, name, sex, age, siblingsOrSpousesAboard, parentsOrChildrenAboard, fare )
       

        db.session.add(new_raw_data)
        db.session.commit()
        return raw_data_schema.jsonify(new_raw_data)
    except:
        print(new_raw_data)
        return jsonify('Bad post data'),400
    
    
# Get All Data
@app.route('/people', methods=['GET'])
def get_datas():
  all_raw_data = Raw_data.query.all()
  result = raw_datas_schema.dump(all_raw_data)
  return jsonify(result.data)


# Get Single Data
@app.route('/people/<uuid>', methods=['GET'])
def get_data(uuid):
  try:
      data = Raw_data.query.get(uuid)
      if data is None:
          return jsonify('Not Found'),404
      return raw_data_schema.jsonify(data)
  except:
      return jsonify('Misunderstood Request'),400


# Update a Data
@app.route('/people/<uuid>', methods=['PUT'])
def update_data(uuid):
  try:
      data = Raw_data.query.get(uuid)
  except:
      return jsonify('Request is not UUID'),401

  if data is None:
      return jsonify('Not Found'),404

  try:
      survived = request.json['survived']
      passengerClass = request.json['passengerClass']
      name = request.json['name']
      sex = request.json['sex']
      age = request.json['age']
      siblingsOrSpousesAboard = request.json['siblingsOrSpousesAboard']
      parentsOrChildrenAboard = request.json['parentsOrChildrenAboard']
      fare = request.json['fare']

      data.survived = survived
      data.passengerClass = passengerClass
      data.name = name
      data.sex = sex
      data.age = age
      data.siblingsOrSpousesAboard = siblingsOrSpousesAboard
      data.parentsOrChildrenAboard = parentsOrChildrenAboard
      data.fare = fare

      db.session.commit()
      return jsonify("Updated: {}".format(uuid))
      
  except:
      return jsonify('Misunderstood Request'),400

    
# Delete Data
@app.route('/people/<uuid>', methods=['DELETE'])
def delete_data(uuid):
  try:
      data = Raw_data.query.get(uuid)
  except:
      return jsonify('Misunderstood Request'),400

  if data is None:
      return jsonify('Not Found'),404
  db.session.delete(data)
  db.session.commit()
   
  return jsonify("Deleted: {}".format(uuid))