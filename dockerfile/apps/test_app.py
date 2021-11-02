from flask import request, jsonify
import os
import tempfile
import pytest
from app import app


# @app.route('/api/auth')
# def auth():
#     json_data = request.get_json()
#     email = json_data['email']
#     password = json_data['password']
#     return jsonify(token=generate_token(email, password))

# with app.test_client() as c:
#     rv = c.post('/api/auth', json={
#         'email': 'flask@example.com', 'password': 'secret'
#     })
#     json_data = rv.get_json()
#     assert verify_token(email, json_data['token'])




@pytest.fixture
def client():
    #db_fd, db_path = tempfile.mkstemp()
    app.config["TESTING"]=True
    with app.test_client() as client:
        yield client

def test_test1(client):
#with app.test_client() as c:
    rv = client.post('/predict', json={
         "school":"GP",
         "sex":"F",
         "age":15,
         "address":"U",
         "famsize":"LE3",
         "Pstatus":"T",
         "Medu":0,
         "Fedu":0,
         "Mjob":"teacher",
         "FJob":"teacher",
         "reason":"home",
         "guardian":"mother",
         "traveltime":1,
         "studytime":1,
         "failures":1,
         "schoolsup":True,
         "famsup":True,
         "paid":True,
         "activities":True,
         "nursery":True,
         "higher":True,
         "internet":True,
         "romantic":True,
         "famrel":1,
         "freetime":1,
         "goout":1,
         "Dalc":1,
         "Walc":1,
         "health":1,
         "absences":0
     })
    json_data = rv.get_json()
    print("hello\n")
    print(json_data)
    assert True
    

 