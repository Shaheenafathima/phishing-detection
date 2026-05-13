import pandas as pd
import re
from urllib.parse import urlparse

# Function to extract features
def extract_features(url):
    parsed = urlparse(url)
    
    domain = parsed.netloc
    
    return [
        len(url),                          # URL length
        url.count('.'),                    # number of dots
        url.count('-'),                    # hyphens
        url.count('@'),                    # @ symbol
        url.count('?'),                    # question mark
        url.count('%'),                    # %
        url.count('='),                    # =
        len(domain),                       # domain length
        1 if parsed.scheme == 'https' else 0,  # https or not
        1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0,  # IP address
        1 if "login" in url.lower() else 0,
        1 if "bank" in url.lower() else 0,
        1 if "verify" in url.lower() else 0,
        1 if "secure" in url.lower() else 0,
    ]

# Load dataset
data = pd.read_csv("final_dataset.csv")

# Apply feature extraction
features = data['url'].apply(lambda x: extract_features(x))

# Convert to dataframe
feature_df = pd.DataFrame(features.tolist(), columns=[
    'url_length','dots','hyphens','at','question','percent','equal',
    'domain_length','https','ip_address','login_word','bank_word',
    'verify_word','secure_word'
])

# Combine with label
final_data = pd.concat([feature_df, data['label']], axis=1)

# Save dataset
final_data.to_csv("featured_dataset.csv", index=False)

print("✅ Feature extraction completed!")
print(final_data.head())