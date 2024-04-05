import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Load the dataset
data = pd.read_csv('Smishing_dataset.csv')

# Check for missing values in the 'message' column
missing_values = data['message'].isnull().sum()
print("Number of missing values in 'message' column:", missing_values)

# Handle missing values
data['message'].fillna("", inplace=True)  # Replace missing values with empty string

# Preprocess the data
data['message'] = data['message'].apply(lambda x: x.lower())
data['label'] = data['label'].apply(lambda x: 1 if x == 'smishing' else 0)

# Split the data into features and labels
X = data['message']
y = data['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text data into numerical features
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train the Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_vectorized, y_train)

# Evaluate the model
accuracy = clf.score(X_test_vectorized, y_test)
print(f"Accuracy: {accuracy}")

# Detect smishing messages
def detect_smishing(message):
    message_vectorized = vectorizer.transform([message])
    prediction = clf.predict(message_vectorized)
    if prediction[0] == 1:
        print("The message is likely a smishing attempt.")
    else:
        print("The message appears to be legitimate.")

# Example usage
detect_smishing("Free gift card! Click here to claim: https://example.com/gift")
detect_smishing("Hi, this is your bank. Please update your account information.")
