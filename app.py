from flask import Flask, render_template, request, redirect, url_for
import joblib

application = app = Flask(__name__)

# Try to load the models with exception handling
cd_model, ht_model = None, None

try:
    cd_model = joblib.load('voting_clf_CD.joblib')
    print("CD Not model loaded successfully.")
except Exception as e:
    print(f" CD Not  model loaded successfully: {str(e)}")

try:
    ht_model = joblib.load('voting_clf_HT.joblib')
    print("HT model loaded successfully.")
except Exception as e:
    print(f"HT model loaded successfully. {str(e)}")

# Define the login page
@app.route('/')
def login():
    return render_template('login.html')

# Define the login authentication route
@app.route('/login', methods=['POST'])
def login_action():
    username = request.form['username']
    password = request.form['password']
    
    # Check if the login details are correct
    if username == 'Admin' and password == 'Admin':
        return redirect(url_for('welcome'))
    else:
        error = "Invalid Username or Password"
        return render_template('login.html', error=error)

# Define the welcome page where user inputs their health data
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

# Define the route that handles the prediction submission
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    cholesterol = float(request.form['cholesterol'])
    diastolic_bp = float(request.form['diastolic_bp'])
    systolic_bp = float(request.form['systolic_bp'])
    diabetes = int(request.form['diabetes'])
    family_history = int(request.form['family_history'])
    bp_status = int(request.form['blood_pressure_status'])

    # Check if models were loaded successfully before making predictions
    if cd_model and ht_model:
        # Prepare the input data as a 2D array for the models
        input_data = [[cholesterol, diastolic_bp, systolic_bp, diabetes, family_history, bp_status]]

        try:
            # Predict Coronary Artery Disease (CAD) using the loaded model
            cad_prediction = cd_model.predict(input_data)[0]
            cad_risk = "High Risk of CAD" if cad_prediction == 1 else "Low Risk of CAD"
        except Exception as e:
            cad_risk = f"Error in CAD prediction: {str(e)}"

        try:
            # Predict Hypertension (HT) using the loaded model
            ht_prediction = ht_model.predict(input_data)[0]
            hypertension_risk = "Hypertension" if ht_prediction == 1 else "Normal Blood Pressure"
        except Exception as e:
            hypertension_risk = f"Error in HT prediction: {str(e)}"
    else:
        # Fallback if models were not loaded
        cad_risk = "CAD model not available"
        hypertension_risk = "HT model not available"

    # Pass the results to the result.html template
    return render_template('result.html', cad_risk=cad_risk, hypertension_risk=hypertension_risk)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)