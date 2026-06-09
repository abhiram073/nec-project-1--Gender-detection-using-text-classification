from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        name = request.form['name']

    # Transform input
        transformed_name = vectorizer.transform([name])

        # Predict gender
        prediction = model.predict(transformed_name)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=False)     