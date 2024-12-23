# preprocessing/preprocessor.py
"""
Preprocessor module for loading and cleaning data for the fraud detection system.
"""

import pandas as pd
import numpy as np

def load_data(filepath):
    """
    Load raw data from a CSV file.
    :param filepath: Path to the CSV file.
    :return: Pandas DataFrame containing the data.
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError as e:
        raise Exception(f"File not found: {filepath}") from e

def clean_data(data):
    """
    Clean and preprocess the raw data.
    :param data: Raw data as a Pandas DataFrame.
    :return: Processed DataFrame ready for analysis.
    """
    # Fill missing values
    data.fillna(0, inplace=True)

    # Convert categorical columns to numeric (example)
    for column in data.select_dtypes(include=['object']).columns:
        data[column] = pd.factorize(data[column])[0]

    # Normalize numerical columns
    for column in data.select_dtypes(include=['int64', 'float64']).columns:
        data[column] = (data[column] - data[column].mean()) / data[column].std()

    return data
