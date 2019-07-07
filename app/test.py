
from api import app
from flask import json


def test_get_passenger():
    response = app.test_client().get(   
        '/people',
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data == []

def test_add_passenger():        
    response = app.test_client().post(
        '/people',
        data=json.dumps({ "survived": 0, "passengerClass": 3, "name": "Mr. Owen Harris Braund", "sex": "male", "age": 22, "siblingsOrSpousesAboard": 1, "parentsOrChildrenAboard":0, "fare":7.25 }),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['age'] == 22.0
    assert data['fare'] == 7.25
    assert data['name'] == "Mr. Owen Harris Braund"
    assert data['parentsOrChildrenAboard'] == 0
    assert data['passengerClass'] == 3
    assert data['sex'] == "male"
    assert data['siblingsOrSpousesAboard'] == 1
    assert data['survived'] == False
    global uuid
    uuid = data['uuid']
    
def test_update_passenger():        
    response = app.test_client().put(
        '/people/' + uuid ,
        data=json.dumps({ "survived": 1, "passengerClass": 1, "name": "Ms. Braund", "sex": "female", "age": 35.5, "siblingsOrSpousesAboard": 10, "parentsOrChildrenAboard":10, "fare":27.55 }),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
   
   
def test_get_specific_passenger():
    response = app.test_client().get(   
        '/people/' + uuid,
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['age'] == 35.5
    assert data['fare'] == 27.55
    assert data['name'] == 'Ms. Braund'
    assert data['parentsOrChildrenAboard'] == 10
    assert data['passengerClass'] == 1
    assert data['sex'] == "female"
    assert data['siblingsOrSpousesAboard'] == 10
    assert data['survived'] == True

def test_delete_passenger():
    response = app.test_client().delete(   
        '/people/' + uuid,
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    
def test_get_deleted_passenger():
    response = app.test_client().get(   
        '/people/' + uuid,
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 404
    assert data == 'Not Found'