import pandas as pd

# Load dataset
data = pd.read_csv("top-1m.csv", header=None)

# Rename columns
data.columns = ['rank', 'domain']

# Take only top N websites (example: 5000)
data = data.head(5000)

# Convert to proper URL format
data['url'] = "https://" + data['domain']

# Add label (0 = legitimate)
data['label'] = 0

# Keep only required columns
final_data = data[['url', 'label']]

# Save file
final_data.to_csv("legitimate_urls.csv", index=False)

print("✅ Legitimate dataset ready!")