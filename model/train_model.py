# models/train_model.py
"""
Module for training and saving the machine learning model for fraud detection.
"""

import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model(data, target_column, model_path):
    """
    Train a RandomForest model and save it to a file.
    :param data: DataFrame containing the features and target column.
    :param target_column: Name of the column containing labels.
    :param model_path: Path to save the trained model.
    """
    # Split data into features and labels
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy:.2f}")

    # Save model to file
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

def load_model(model_path):
    """
    Load a trained model from a file.
    :param model_path: Path to the model file.
    :return: Loaded model.
    """
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model
