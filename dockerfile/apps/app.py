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
    try:
        age = request.args.get('age')
        absences = request.args.get('absences')
        health = request.args.get('health')
        walc = request.args.get('Walc')
        dalc = request.args.get('Dalc')
    except:
        return jsonify(-1)
    else:
        data = [[age],[health],[absences], [walc], [dalc]]
        query_df = pd.DataFrame({'Walc': pd.Series(walc),
                                'Dalc' : pd.Series(dalc),
                                'absences' : pd.Series(absences),
                                'age' : pd.Series(age),
                                'health' : pd.Series(health)})
        prediction = clf.predict(query_df)
        return jsonify(np.asscalar(prediction))


if __name__ == '__main__':
    clf = joblib.load('/apps/model.pkl')
    app.run(host="0.0.0.0", debug=True)