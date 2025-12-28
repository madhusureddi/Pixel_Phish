@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('url')
    if not url:
        return render_template('index.html', error="URL enters cheyandi.")

    # --- ML Prediction using model.pkl + feature.py ---
    from feature import FeatureExtraction
    import numpy as np
    import pickle

    file = open("pickle/model.pkl", "rb")
    gbc = pickle.load(file)
    file.close()

    obj = FeatureExtraction(url)
    x = np.array(obj.getFeaturesList()).reshape(1, 30)
    y_pred = gbc.predict(x)[0]
    y_pro_non_phishing = gbc.predict_proba(x)[0,1]
    prediction = "Safe" if y_pred == 1 else "Unsafe"

    return render_template('index.html', url=url, result=prediction)
