# Entry point of the project: `app.py`

# app.py
"""
Main script to orchestrate the transactional fraud detection system.
Contains steps for data ingestion, preprocessing, model inference, and fraud alerts.
"""
import preprocessing.preprocessor as preprocessor
import models.train_model as train_model
import detection.anomaly_detection as anomaly_detection
import utils.logger as logger

# Entry function
def main():
    logger.log("Starting fraud detection system")

    # Step 1: Load data
    data = preprocessor.load_data("data/raw/sample_data.csv")

    # Step 2: Preprocess data
    processed_data = preprocessor.clean_data(data)

    # Step 3: Load trained model
    model = train_model.load_model("models/model.pkl")

    # Step 4: Detect fraud
    predictions = anomaly_detection.detect_fraud(processed_data, model)

    # Step 5: Generate report
    logger.log(f"Fraud detected in {sum(predictions)} transactions")

if __name__ == "__main__":
    main()
