
from api import app
from flask import json

def test_get_config():
    response = app.test_client().get(   
        '/people',
        content_type='application/json',
    )

    #data = json.loads(response.get_data(as_text=True))

    #assert response.status_code == 200
    #assert data == []