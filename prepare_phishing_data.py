import pandas as pd

# Load PhishTank dataset
df = pd.read_csv("phishing_urls.csv")

# Keep only URL column
df = df[['url']]

# Add label (1 = phishing)
df['label'] = 1

# Save new file
df.to_csv("phishing_urls.csv", index=False)

print("✅ Phishing dataset prepared successfully")