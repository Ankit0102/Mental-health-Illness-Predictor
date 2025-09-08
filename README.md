# 🧠 Mental Health Illness Predictor

A professional, open-source solution for workplace mental health screening powered by machine learning.

---

## Project Overview

**Title:** Mental Health Illness Predictor

**Description:**  
A web-based application that predicts whether an individual may require mental health treatment, based on personal and workplace factors. The prediction is made using a trained machine learning model and a simple, user-friendly web interface.

**Industry Context & Use Cases:**  
This project is designed for the **HR, healthcare, and tech industries** where mental health screening and awareness are critical.  
**Use cases include:**  
- HR departments assessing employee well-being.
- Occupational health professionals conducting anonymous screenings.
- Tech companies enabling easy self-assessment for remote workers and teams.

**Key Features & Benefits:**
- **Easy-to-use interface:** No technical expertise required.
- **Instant prediction:** Immediate feedback on mental health needs.
- **Customizable input:** Gathers key workplace and demographic factors.
- **Privacy-first:** All data is processed locally; no cloud or external API required.
- **Scalable:** Can be deployed for teams, companies, or as a public service.

**Target Audience:**
- Developers and data scientists (for extension/customization)
- HR and wellness professionals
- Businesses with a focus on employee mental health
- End-users seeking privacy-friendly self-assessment

---

## Technical Documentation

### Installation

**Prerequisites:**
- Python 3.7+
- `pip` (Python package manager)
- A trained ML model saved as `model.pkl` in the project root

**Setup:**
```bash
git clone https://github.com/Ankit0102/Mental-health-Illness-Predictor.git
cd Mental-health-Illness-Predictor
pip install flask numpy scikit-learn
```

**Note:**  
You must provide your own `model.pkl` that matches the input format.

### Usage Example

**Start the Application:**
```bash
python app.py
```
Open your browser to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

**Sample Interaction:**
- Fill in fields like Age, Gender, self_employed, family_history, work_interfere, etc.
- Click **Predict** to receive instant feedback.

**Backend Code Example:**
```python
@application.route("/prediction", methods=["POST"])
def prediction():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
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

- The model must be trained and saved as `model.pkl` with scikit-learn.
- Input fields in `pred.html` match model features. Edit `pred.html` to add/remove fields.

### Dependencies

- Python 3.7+
- Flask
- NumPy
- scikit-learn
- Pickle (for model serialization)

---

## Professional Elements

**Badges:**  
*(Add badges for build status, license, version as needed. Example:)*  
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green)

**License:**  
No explicit license is found. Please add a license (MIT recommended) for open-source compliance.

**Screenshots:**  
*(No screenshots found in repo, add UI screenshots for best results.)*

**Demo:**  
To run a local demo, follow usage instructions above.

**Architecture Overview:**  
- **Frontend:** HTML/CSS form (`pred.html`, `styles.css`)
- **Backend:** Flask app (`app.py`)
- **ML Model:** `model.pkl` loaded into memory
- **Flow:**  
    1. User submits form  
    2. Flask backend parses input  
    3. Model returns prediction  
    4. Result displayed on UI

**Performance Metrics:**  
*(No benchmarks found; add model accuracy, inference time, etc. if available.)*

---

## Community & Support

**Contributing:**  
Fork the repository, create a branch, and submit a pull request.  
*(No CONTRIBUTING.md found; add for more details.)*


**Changelog / Roadmap:**  
*(No changelog detected; consider adding one for version tracking.)*

---

## Industry-Specific Considerations

**Compliance:**  
No direct references to GDPR, HIPAA, or SOC2.  
- **Note:** For production use, ensure secure handling of user data and compliance with relevant regulations.

**Security:**  
- All predictions run locally.
- No data is sent externally.
- No authentication implemented; add for production.

**Scalability:**  
- Stateless Flask app; can be containerized and deployed on cloud or on-premise servers.
- For large organizations, run behind a secure proxy/load balancer.

**Integration:**  
- Can be integrated with HR tools via API endpoints.
- Extendable for additional data sources or reporting.

---

## File Structure

```
├── app.py              # Flask backend logic
├── pred.html           # Main HTML form
├── styles.css          # UI styling
├── model.pkl           # ML model (must be provided)
```

---

## Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [Python Pickle](https://docs.python.org/3/library/pickle.html)

---

## Maintainer

Developed by [Ankit0102](https://github.com/Ankit0102).

---

*Disclaimer: This tool is for educational and awareness purposes only. Not medical advice. For professional help, consult a qualified mental health provider.*
