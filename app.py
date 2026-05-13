from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from feature_extraction import extract_features
import datetime

app = Flask(__name__)

# Load dataset
data = pd.read_csv("featured_dataset.csv")
X = data.drop('label', axis=1)
y = data['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    
    # Extract features
    features = extract_features(url)
    
    # Prediction
    prediction = model.predict([features])[0]
    probability = model.predict_proba([features])[0][prediction]

    # Result
    if prediction == 1:
        result = "⚠️ Phishing Website"
    else:
        result = "✅ Legitimate Website"

    # Save history (FIXED UTF-8)
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} | {url} | {result} | {round(probability*100,2)}%\n")

    return render_template("index.html",
                           prediction_text=result,
                           prob=f"{round(probability*100,2)}%",
                           url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
