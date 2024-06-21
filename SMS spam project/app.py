from flask import Flask, render_template, request
 #render_template is used to render HTML templates
#request is used to handle incoming data from a client.

import pickle
 #pickle is used to load the pre-trained model and vectorizer
import numpy as np

model = pickle.load(open('spamclassifier_MnB.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            messg = str(request.form['mesg'])
            transformed = vectorizer.transform([messg])
            transformed_data = transformed.toarray()
            pred = model.predict(transformed_data)
            output = str(pred[0])
            return render_template('result.html',prediction=f"{output}")
    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
