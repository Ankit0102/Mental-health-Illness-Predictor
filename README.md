# 🧠 Mental Health Illness Predictor

A professional, open-source solution for workplace mental health screening powered by machine learning.

---

## Project Overview

**Title:** Mental Health Illness Predictor

**Description:**  
A web-based application that predicts whether an individual may require mental health treatment, based on personal and workplace factors. The prediction is made using a trained machine learning model and a simple, user-friendly web interface. The model is trained using `train_model.py` and uses the following features: Age, Gender, Country, Self Employed, Family History. The target variable is `treatment` (Yes/No).

---

## Technical Documentation

### Installation & Setup

**Prerequisites:**
- Python 3.10+
- `pip` (Python package manager)

**Setup:**
```powershell
git clone https://github.com/Ankit0102/Mental-health-Illness-Predictor.git
cd Mental-health-Illness-Predictor
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

**Training the Model:**
```powershell
python train_model.py
```

**Running the App:**
```powershell
python app.py
```
Open your browser to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

**Sample Interaction:**
- Fill in fields: Age, Gender, Country, Self Employed, Family History.
- Click **Predict** to receive instant feedback.

**Backend Code Example:**
```python
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
```

### API Documentation
- **POST /prediction:** Receives form data, returns prediction text.
- No external API calls; all processing is local.

### Configuration Options
- The model is trained and saved as `model.pkl` using `train_model.py`.
- Input fields in `pred.html` match model features. Edit `pred.html` to add/remove fields.

### Dependencies
- Python 3.10+
- Flask
- NumPy
- scikit-learn
- pandas
- Pickle (for model serialization)

---

## File Structure

```
├── app.py                # Flask backend logic
├── train_model.py        # Model training and saving
├── requirements.txt      # Python dependencies
├── survey.csv            # Data file
├── model.pkl             # ML model (auto-generated)
├── styles.css            # UI styling
└── templates/
    └── pred.html         # Main HTML form (must be in templates folder)
```

---

*Disclaimer: This tool is for educational and awareness purposes only. Not medical advice. For professional help, consult a qualified mental health provider.*
