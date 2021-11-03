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

def test_client(client):
    rv = client.get('/predict',query_string = dict(age = 18,health=2, absences=90,Dalc=1,Walc=4))
    print("\n====== Result TEST_CLIENT ======")
    print(rv.data)
    print("TEST PASSED!")

#@app.route('/predict?age=18&health=2&absences=90&Dalc=1&Walc=4')
def test_predict1(client):
    rv = client.get('/predict',query_string = dict(age = 18,health=2, absences=90,Dalc=1,Walc=4))
    json_data = rv.get_json()
    print("the result is ",json_data)
    assert json_data ==1
    print("TEST PASSED!")


def test_predict2(client):
    r = client.get('/predict',query_string = dict(age = 18,health=2, absences=90,Dalc=1,Walc=4))
    print("\n====== Result TEST_PREDICT ======")
    print(int(r.data))
    assert(int(r.data) == 1)
    print("TEST PASSED!")
 
def test_predict_bad_value(client):
    r = client.get('/predict',query_string = dict(age = 15,health=2, absences=-10,Dalc=4,Walc=-1))
    print("\n====== Result TEST_PREDICT ======")
    print(int(r.data))
    assert(int(r.data) == -1)
    print("TEST PASSED!")

def test_predict_missing_value(client):
    r = client.get('/predict',query_string = dict(age = 18,health=2, absences=-90))
    print("\n====== Result TEST_PREDICT ======")
    print(int(r.data))
    assert(int(r.data) == -1)
    print("TEST PASSED!")