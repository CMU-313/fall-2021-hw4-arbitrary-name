from flask import request, jsonify
import os
import tempfile
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"]=True
    with app.test_client() as client:
        yield client

#@app.route('/predict?age=18&health=2&absences=90&Dalc=1&Walc=4')
def test_test1(client):
    rv = client.get('/predict',query_string = dict(age = 18,health=2, absences=90,Dalc=1,Walc=4))
    json_data = rv.get_json()
    print("the result is ",json_data)
    assert json_data ==1


    

 
