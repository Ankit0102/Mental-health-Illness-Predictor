import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Load data
df = pd.read_csv('survey.csv')

# Basic cleaning: drop rows with missing target
df = df.dropna(subset=['treatment'])

# Encode categorical columns
for col in ['Gender', 'Country', 'self_employed', 'family_history']:
    df[col] = df[col].fillna('Unknown')
    df[col] = LabelEncoder().fit_transform(df[col])

# Define features and target
X = df[['Age', 'Gender', 'Country', 'self_employed', 'family_history']]
y = df['treatment'].map({'Yes': 1, 'No': 0})

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
