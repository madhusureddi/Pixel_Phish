from flask import Flask, render_template, request
import numpy as np
import pickle
from feature import FeatureExtraction

# Initialize Flask app
app = Flask(__name__)

# Load ML model
with open("pickle/model.pkl", "rb") as file:
    gbc = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html', xx=-1, url="")

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('url')
    if not url:
        return render_template('index.html', xx=-1, url="", error="Please enter a URL.")

    # --- ML Prediction ---
    try:
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1, 30)
        y_pred = gbc.predict(x)[0]           # 1 = safe, -1 = unsafe
        y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        prediction = "Safe" if y_pred == 1 else "Unsafe"

        return render_template('index.html', xx=round(y_pro_non_phishing,2), url=url, result=prediction)

    except Exception as e:
        return render_template('index.html', xx=-1, url=url, error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
