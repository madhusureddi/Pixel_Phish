from flask import Flask, render_template, request
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# --- 1. Flask App Initialization (NameError Fix) ---
app = Flask(__name__) #

# --- 2. Gemini Config (404 Error Fix) ---
genai.configure(api_key="AIzaSyB_yxxTE7tBD_F8UnTDscPBiGTI-nh1nq0") #

# retired 1.5 badulu Gemini 2.5 flash vaadandi
model = genai.GenerativeModel('gemini-2.5-flash') 

# --- 3. Firebase Setup ---
cred = credentials.Certificate("serviceAccountKey.json") #
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('url')
    if not url:
        return render_template('index.html', error="URL enters cheyandi.")

    try:
        # Prompt logic
        prompt = f"Analyze this URL: {url}. Return ONLY one word: Benign, Phishing, or Malware."
        response = model.generate_content(prompt)
        prediction = response.text.strip()

        # Save to Firebase
        db.collection('url_logs').add({
            'url': url,
            'result': prediction,
            'timestamp': datetime.now()
        })

        return render_template('index.html', url=url, result=prediction)

    except Exception as e:
        # Debugging kosam error ni display chesthunnam
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)