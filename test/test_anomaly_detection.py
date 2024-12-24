import pytest
import pandas as pd
from detection.anomaly_detection import AnomalyDetector

# Dummy data for testing
@pytest.fixture
def setup_test_data():
    data = {
        "transaction_id": [1, 2, 3, 4],
        "amount": [100, 5000, 200, 10000],
        "currency": ["USD", "USD", "USD", "USD"],
    }
    df = pd.DataFrame(data)
    return df

# Test: Initialization of AnomalyDetector
def test_anomaly_detector_initialization():
    detector = AnomalyDetector(threshold=0.8)
    assert detector.threshold == 0.8

# Test: Anomaly detection process
def test_detect_anomalies(setup_test_data):
    detector = AnomalyDetector(threshold=0.5)
    results = detector.detect_anomalies(setup_test_data)
    
    # Ensure results contain necessary columns
    assert "anomaly_score" in results.columns
    assert "is_anomaly" in results.columns
    
    # Check that anomalies are correctly identified
    assert results["is_anomaly"].sum() > 0  # At least one anomaly detected

# Test: Edge case for empty data
def test_empty_data():
    detector = AnomalyDetector(threshold=0.5)
    empty_df = pd.DataFrame(columns=["transaction_id", "amount", "currency"])
    results = detector.detect_anomalies(empty_df)
    
    # Ensure no anomalies are detected in an empty dataset
    assert results.empty

# Test: Handling invalid data
def test_invalid_data():
    detector = AnomalyDetector(threshold=0.5)
    invalid_df = pd.DataFrame({"invalid_column": [1, 2, 3]})
    
    with pytest.raises(KeyError):
        detector.detect_anomalies(invalid_df)
