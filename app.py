from flask import Flask, render_template, request
import os
import numpy as np

from src.datascience import logger
from src.datascience.pipeline.prdiction_pipeline import PredictionPipeline


app = Flask(__name__)

@app.route('/', methods = ['GET'])  # homepage
def homepage():
    return render_template('index.html')

@app.route('/train', methods=['GET']) # route to train the model 
def training():
    logger.info("Training Started")
    os.system("python main.py")
    logger.info("Training Successful")
    return "Training Completed Successfully"

@app.route("/predict", methods=['POST', 'GET']) # route from web ui
def predict():
    if request.method == 'POST':
        try:
            # Extract values as floats (remove trailing commas)
            fixed_acidity = float(request.form.get('fixedAcidity'))
            volatile_acidity = float(request.form.get('volatileAcidity'))
            citric_acid = float(request.form.get('citricAcid'))
            residual_sugar = float(request.form.get('residualSugar'))
            chlorides = float(request.form.get('chlorides'))
            free_sulfur_dioxide = float(request.form.get('freeSulfurDioxide'))
            total_sulfur_dioxide = float(request.form.get('totalSulfurDioxide'))
            density = float(request.form.get('density'))
            pH = float(request.form.get('pH'))
            sulphates = float(request.form.get('sulphates'))
            alcohol = float(request.form.get('alcohol'))

            data = {
                'fixed_acidity': float(request.form.get('fixedAcidity')),
                'volatile_acidity': float(request.form.get('volatileAcidity')),
                'citric_acid': float(request.form.get('citricAcid')),
                'residual_sugar': float(request.form.get('residualSugar')),
                'chlorides': float(request.form.get('chlorides')),
                'free_sulfur_dioxide': float(request.form.get('freeSulfurDioxide')),
                'total_sulfur_dioxide': float(request.form.get('totalSulfurDioxide')),
                'density': float(request.form.get('density')),
                'pH': float(request.form.get('pH')),
                'sulphates': float(request.form.get('sulphates')),
                'alcohol': float(request.form.get('alcohol'))
            }

            # Prepare the input for prediction
            input_data = np.array([
                fixed_acidity, volatile_acidity, citric_acid,
                residual_sugar, chlorides, free_sulfur_dioxide,
                total_sulfur_dioxide, density, pH, sulphates, alcohol
            ]).reshape(1, -1)

            # Call your prediction pipeline
            prediction_pipeline = PredictionPipeline()
            prediction = prediction_pipeline.predict(input_data)

            return render_template('result.html', prediction=prediction, data=data)

        except Exception as e:
            logger.error(f"Error occurred: {e}")
            return f"Error: {str(e)}"
    else:
        return render_template('index.html')
    

if __name__  == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)