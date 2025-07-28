# prepare_dataset.py

import pandas as pd

# Load datasets
fake = pd.read_csv('Fake.csv')
true = pd.read_csv('True.csv')

# Add labels
fake['label'] = 1
true['label'] = 0

# Keep only necessary columns
fake = fake[['title', 'text', 'label']]
true = true[['title', 'text', 'label']]

# Combine and shuffle
data = pd.concat([fake, true]).sample(frac=1).reset_index(drop=True)

# Save as train.csv
data.to_csv('train.csv', index=False)

print("✅ train.csv generated successfully.")
