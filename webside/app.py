from flask import Flask, render_template, request, jsonify
import pickle
import os
from flask_material import Material
import pandas as pd
import numpy as np

app = Flask(__name__)
Material(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/preview')
def preview():
    csv_path = r'C:\Users\Srijan\Desktop\Internship\Iris-Classification\Dataset\Iris.csv'
    print(f"CSV Path: {csv_path}")

    # Check if the file exists
    if not os.path.exists(csv_path):
        return "File not found!", 404

    # Read the CSV file
    df = pd.read_csv(csv_path)

    # Convert the dataframe to an HTML table
    df_html = df.to_html(classes='table table-striped', index=False)

    # Render the template with the dataframe passed to it
    return render_template("preview.html", df_view=df_html)


@app.route('/', methods=["POST"])
def analyze():
	if request.method == 'POST':
		petal_length = request.form['petal_length']
		sepal_length = request.form['sepal_length']
		petal_width = request.form['petal_width']
		sepal_width = request.form['sepal_width']
		model_choice = request.form['model_choice']

		# Clean the data by convert from unicode to float
		sample_data = [sepal_length, sepal_width, petal_length, petal_width]
		clean_data = [float(i) for i in sample_data]

		# Reshape the Data as a Sample not Individual Features
		ex1 = np.array(clean_data).reshape(1, -1)

		# Reloading the Model
		# if model_choice == 'logitmodel':
		#     logit_model = joblib.load('data/logit_model_iris.pkl')
		#     result_prediction = logit_model.predict(ex1)
		# elif model_choice == 'knnmodel':
		# 	knn_model = joblib.load('data/knn_model_iris.pkl')
		# 	result_prediction = knn_model.predict(ex1)
		# elif model_choice == 'svmmodel':
		# 	knn_model = joblib.load('data/svm_model_iris.pkl')
		# 	result_prediction = knn_model.predict(ex1)

	return render_template('index.html', petal_width=petal_width,
                        sepal_width=sepal_width,
                        sepal_length=sepal_length,
                        petal_length=petal_length,
                        clean_data=clean_data,
                        # result_prediction=result_prediction,
                        model_selected=model_choice)


if __name__ == '__main__':
    # production
    # serve(app, host="localhost", port=4000)
    # Development
    app.run(debug=True, host='localhost', port=4000)
