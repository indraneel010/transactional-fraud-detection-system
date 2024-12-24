
import pytest
import os
from preprocessing.preprocessor import Preprocessor

# Test data path
RAW_DATA_PATH = "data/raw/sample_data.csv"
PROCESSED_DATA_PATH = "data/processed/processed_data.csv"

# Fixture to set up and clean up test environment
@pytest.fixture
def setup_test_environment(tmp_path):
    # Create dummy raw data for testing
    raw_data_content = "transaction_id,amount,currency,fraud_flag\n1,100,USD,0\n2,200,EUR,1"
    test_raw_data_path = tmp_path / "sample_data.csv"
    with open(test_raw_data_path, "w") as f:
        f.write(raw_data_content)
    return str(test_raw_data_path)

# Test: Initialization of Preprocessor
def test_preprocessor_initialization(setup_test_environment):
    preprocessor = Preprocessor(input_path=setup_test_environment, output_path=PROCESSED_DATA_PATH)
    assert preprocessor.input_path == setup_test_environment
    assert preprocessor.output_path == PROCESSED_DATA_PATH

# Test: Data cleaning functionality
def test_data_cleaning(setup_test_environment):
    preprocessor = Preprocessor(input_path=setup_test_environment, output_path=PROCESSED_DATA_PATH)
    processed_data = preprocessor.clean_data()
    assert not processed_data.isnull().values.any()  # Ensure no null values
    assert processed_data.shape[1] == 4  # Check correct number of columns

# Test: Data saving functionality
def test_save_cleaned_data(setup_test_environment, tmp_path):
    processed_output_path = tmp_path / "processed_data.csv"
    preprocessor = Preprocessor(input_path=setup_test_environment, output_path=str(processed_output_path))
    preprocessor.clean_data()
    preprocessor.save_cleaned_data()
    assert os.path.exists(processed_output_path)  # Check file creation
