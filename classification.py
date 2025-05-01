# 📦 Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split      # For splitting data into training/testing sets
from sklearn.preprocessing import LabelEncoder            # For converting categorical labels into numbers
from sklearn.tree import DecisionTreeClassifier           # The classification algorithm
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix  # For evaluation

# 📥 Step 1: Extract - Load the dataset
# Make sure 'car_evaluation.csv' is in your working directory
data = pd.read_csv('car_evaluation.csv', header=None)

# Assign column names (as the file has no headers)
data.columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']

# Show first few rows
print("Initial Data Preview:")
print(data.head())

# 🔄 Step 2: Transform - Encode all categorical features to numeric values
# Most ML algorithms need numerical input, so we convert categories to numbers
label_encoders = {}
for column in data.columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le  # Save encoder for future inverse_transform or new data

# Split dataset into features (X) and target label (y)
X = data.drop('class', axis=1)   # All columns except 'class'
y = data['class']                # The target variable we want to predict

# Split into training and testing data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🤖 Step 3: Classification - Train a Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# 📊 Step 4: Predict & Evaluate
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.2f}")

# Print a detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Show confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
