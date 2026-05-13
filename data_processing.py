import pandas as pd

# Load datasets
phishing = pd.read_csv("phishing_urls.csv")
legit = pd.read_csv("legitimate_urls.csv")

# Check counts
print("Phishing count:", len(phishing))
print("Legitimate count:", len(legit))

# Balance dataset
min_size = min(len(phishing), len(legit))

phishing = phishing.sample(n=min_size, random_state=42)
legit = legit.sample(n=min_size, random_state=42)

# Combine datasets
data = pd.concat([phishing, legit])

# Shuffle dataset
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Remove duplicates
data = data.drop_duplicates(subset='url')

# Save final dataset
data.to_csv("final_dataset.csv", index=False)

print("✅ Final dataset created!")
print(data.head())