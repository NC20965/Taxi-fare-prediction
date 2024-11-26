import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("xgb_model_final.pkl", "rb"))

@flask_app.route('/Predict', methods=['POST'])
def submit_regression():
    # Get data from the form
    feature1 = request.form.get('feature1')
    feature2 = request.form.get('feature2')
    feature3 = request.form.get('feature3')
    feature4 = request.form.get('feature4')
    target_range = request.form.get('target_range')

    # Mock prediction logic
    try:
        # Convert features to numbers
        f1 = float(feature1)
        f2 = float(feature2)
        f3 = float(feature3) if feature3 else 0
        f4 = float(feature4)

        # Mock regression calculation (adjust as per your model)
        predicted_fare = f1 + f2 + f3 + f4

        # Return the prediction result
        return jsonify({
            "Predicted Fare": round(predicted_fare, 2),
            "Input Features": {
                "Feature1": f1,
                "Feature2": f2,
                "Feature3": f3,
                "Feature4": f4
            }
        })
    except ValueError as e:
        return jsonify({"error": "Invalid input data", "details": str(e)})

if __name__ == '__main__':
    flask_app.run(debug=True)