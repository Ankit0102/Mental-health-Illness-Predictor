import numpy as np
from flask import Flask,request,render_template
import pickle

# Create Flask app
application = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@application.route('/')
def pred():
    return render_template('pred.html')

@application.route("/prediction", methods=["POST"])
def prediction():
    # Get form data in the correct order
    age = float(request.form['Age'])
    gender = request.form['Gender']
    country = request.form['Country']
    self_employed = request.form['self_employed']
    family_history = request.form['family_history']

    # Encode categorical features (same as training)
    from sklearn.preprocessing import LabelEncoder
    le_gender = LabelEncoder().fit(['Male', 'Female', 'Other', 'Unknown'])
    le_country = LabelEncoder().fit([country])
    le_self_employed = LabelEncoder().fit(['Yes', 'No', 'Unknown'])
    le_family_history = LabelEncoder().fit(['Yes', 'No', 'Unknown'])

    gender_encoded = le_gender.transform([gender])[0] if gender in le_gender.classes_ else le_gender.transform(['Unknown'])[0]
    country_encoded = le_country.transform([country])[0]
    self_employed_encoded = le_self_employed.transform([self_employed])[0] if self_employed in le_self_employed.classes_ else le_self_employed.transform(['Unknown'])[0]
    family_history_encoded = le_family_history.transform([family_history])[0] if family_history in le_family_history.classes_ else le_family_history.transform(['Unknown'])[0]

    final_features = np.array([[age, gender_encoded, country_encoded, self_employed_encoded, family_history_encoded]])

    # Make prediction
    prediction = model.predict(final_features)

    # Prepare the prediction message
    if prediction[0] == 1:
        prediction_text = "This person requires mental health treatment"
    else:
        prediction_text = "This person doesn't require mental health treatment"

    return render_template('pred.html', prediction_text=prediction_text)

if __name__ == "__main__":
    application.run(debug=True)
