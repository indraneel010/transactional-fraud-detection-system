# detection/anomaly_detection.py
"""
Module for detecting anomalies in transaction data.
"""

import numpy as np

def detect_fraud(data, model):
    """
    Detect fraud using a machine learning model.
    :param data: Preprocessed data (Pandas DataFrame).
    :param model: Trained machine learning model.
    :return: A list of predictions where 1 indicates fraud and 0 indicates normal transactions.
    """
    # Predict probabilities for each transaction
    probabilities = model.predict_proba(data)[:, 1]

    # Generate fraud predictions based on a threshold
    predictions = (probabilities >= 0.8).astype(int)  # Threshold set to 0.8

    return predictions
