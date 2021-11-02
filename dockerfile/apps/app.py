from flask import Flask, jsonify, request
from sklearn.preprocessing import LabelEncoder
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

@app.route('/predict')
def predict():
	 #use entries from the query string here but could also use json
     #assert(len(request.args) == 30, "Please provide all 30 features") 
     request.args={
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
     }
     query_df = pd.DataFrame(request.args, index=[0])
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/model.pkl')
    app.run(host="0.0.0.0", debug=True)