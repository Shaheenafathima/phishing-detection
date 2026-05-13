import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from feature_extraction import extract_features

# Load trained data
data = pd.read_csv("featured_dataset.csv")

X = data.drop('label', axis=1)
y = data['label']

# Train model again (simple way)
model = RandomForestClassifier()
model.fit(X, y)

# User input
url = input("Enter URL: ")

# Extract features
features = extract_features(url)

# Predict
prediction = model.predict([features])

# Output
if prediction[0] == 1:
    print("⚠️ Phishing Website")
else:
    print("✅ Legitimate Website")