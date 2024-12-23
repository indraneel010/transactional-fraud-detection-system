# config.py
"""
Configuration file for setting paths, thresholds, and constants used across the system.
"""

# File paths
RAW_DATA_PATH = "data/raw/sample_data.csv"
PROCESSED_DATA_PATH = "data/processed/cleaned_data.csv"
MODEL_PATH = "models/model.pkl"

# Fraud detection thresholds
ANOMALY_SCORE_THRESHOLD = 0.8
RULE_BASED_THRESHOLD = 5000  # Transaction value threshold in rule-based detection

# Logging settings
LOG_LEVEL = "INFO"
LOG_FILE = "logs/system.log"
