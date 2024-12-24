import pytest
import os
from models.train_model import ModelTrainer
import joblib

# Paths for test environment
RAW_DATA_PATH = "data/raw/sample_data.csv"
MODEL_OUTPUT_PATH = "models/test_model.pkl"

@pytest.fixture
def setup_training_data(tmp_path):
    # Create dummy training data
    train_data_content = "transaction_id,amount,currency,fraud_flag\n1,100,USD,0\n2,200,EUR,1\n3,150,USD,0\n4,250,EUR,1"
    test_train_data_path = tmp_path / "train_data.csv"
    with open(test_train_data_path, "w") as f:
        f.write(train_data_content)
    return str(test_train_data_path)

# Test: Initialization of ModelTrainer
def test_model_trainer_initialization(setup_training_data):
    trainer = ModelTrainer(data_path=setup_training_data, model_output_path=MODEL_OUTPUT_PATH)
    assert trainer.data_path == setup_training_data
    assert trainer.model_output_path == MODEL_OUTPUT_PATH

# Test: Model training and output
def test_train_model(setup_training_data, tmp_path):
    test_model_path = tmp_path / "test_model.pkl"
    trainer = ModelTrainer(data_path=setup_training_data, model_output_path=str(test_model_path))
    
    # Train the model
    trainer.train_model()
    
    # Check if the model file was created
    assert os.path.exists(test_model_path)
    
    # Load the model and check its type
    model = joblib.load(test_model_path)
    assert hasattr(model, "predict")  # Check if the model has a predict method

# Test: Invalid data handling
def test_invalid_training_data(tmp_path):
    invalid_data_path = tmp_path / "invalid_data.csv"
    with open(invalid_data_path, "w") as f:
        f.write("invalid,data,format\n1,100,abc\n")  # Badly formatted data
    
    trainer = ModelTrainer(data_path=str(invalid_data_path), model_output_path=MODEL_OUTPUT_PATH)
    with pytest.raises(ValueError):  # Replace with appropriate exception
        trainer.train_model()
