from flask import Flask, jsonify, request
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
     age = request.args.get('age')
     absences = request.args.get('absences')
     health = request.args.get('health')
     walc = request.args.get('Walc')
     dalc = request.args.get('Dalc')
     data = [[age],[health],[absences], [walc], [dalc]]
     query_df = pd.DataFrame({ 'age' : pd.Series(age)
                            ,'health' : pd.Series(health) ,
                            'absences' : pd.Series(absences),
                            'Walc': pd.Series(walc),
                            'Dalc' : pd.Series(dalc),
                            })
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    print("i got here")
    clf = joblib.load('/apps/model.pkl')
    app.run(host="0.0.0.0", debug=True)