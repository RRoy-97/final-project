# import dependencies
# from models import create_classes
import os
import numpy as np
# import pickle #Initialize the flask App
from flask import Flask, render_template, jsonify, request, redirect, url_for
# from sklearn import preprocessing
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn import metrics
# from sklearn.metrics import confusion_matrix
# import statsmodels.api as sm
# from sklearn import linear_model
import csv
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# model = pickle.load(open('model.pkl', 'rb'))

#################################################
# Database Setup
#################################################

# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# Loan = create_classes(db)

# create route that renders index.html template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")

@app.route('/about', methods=['GET', 'POST'])
def root(): 
    if request.method == 'GET':
        return render_template('about.html')
    elif request.method == 'POST':
        results = []
        
        user_csv = request.form.get('user_csv').split('\n')
        reader = csv.DictReader(user_csv)
        
        for row in reader:
            results.append(dict(row))

        fieldnames = [key for key in results[0].keys()]

        return render_template('about.html', results=results, fieldnames=fieldnames, len=len)


# Render prediction
# @app.route("/predict", methods=["GET", "POST"])

# def predict():
#     #For rendering results on HTML GUI
#     int_features = [float(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)
#     output = round(prediction[0], 2) 

#     return render_template('index.html', prediction_text='Liklihood of loan default is :{}'.format(output))


#Render results
# @app.route('/results',methods=['POST'])

# def results():

#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
