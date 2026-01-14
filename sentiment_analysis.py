import pandas as pd

# Load datasets (files are in the same folder)
train_data = pd.read_csv("twitter_training.csv")
val_data = pd.read_csv("twitter_validation.csv")

# Rename columns (dataset has no headers)
train_data.columns = ['id', 'entity', 'sentiment', 'text']
val_data.columns = ['id', 'entity', 'sentiment', 'text']

# Keep only required columns
train_data = train_data[['text', 'sentiment']]
val_data = val_data[['text', 'sentiment']]

# Remove empty rows
train_data.dropna(inplace=True)
val_data.dropna(inplace=True)

# Show sample data
print("Training data sample:")
print(train_data.head())

print("\nValidation data sample:")
print(val_data.head())
