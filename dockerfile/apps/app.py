from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)
clf = joblib.load('model.pkl')

@app.route('/')
def hello():
    print("i am in hello")
    return jsonify("try the predict route it is great!")

@app.route('/predict')
def predict():
     age = request.args.get('age')
     absences = request.args.get('absences')
     health = request.args.get('health')
     walc = request.args.get('Walc')
     dalc = request.args.get('Dalc')
     data = [[age],[health],[absences], [walc], [dalc]]
     query_df = pd.DataFrame({ 'age' : pd.Series(age),
                            'health' : pd.Series(health) ,
                            'absences' : pd.Series(absences),
                            'Walc': pd.Series(walc),
                            'Dalc' : pd.Series(dalc),
                            })
     prediction = clf.predict(query_df)
     return jsonify(np.asscalar(prediction))


if __name__ == '__main__':
    app.run(host="0.0.0.0.0", debug=True)
