import os
import logging
import pytest
from utils.logger import setup_logger

@pytest.fixture
def test_logger(tmp_path):
    # Temporary directory for logs during tests
    log_dir = tmp_path / "logs"
    log_dir.mkdir()
    log_file = log_dir / "test.log"
    logger = setup_logger("test_logger", log_file)
    return logger, log_file

def test_logger_initialization(test_logger):
    logger, log_file = test_logger

    # Check logger name
    assert logger.name == "test_logger"

    # Check default logging level
    assert logger.level == logging.DEBUG

def test_log_file_creation(test_logger):
    _, log_file = test_logger

    # Check if log file is created
    assert os.path.exists(log_file)

def test_logging_at_levels(test_logger):
    logger, log_file = test_logger

    # Log messages at different levels
    logger.info("Info message")
    logger.debug("Debug message")
    logger.error("Error message")

    with open(log_file, "r") as f:
        logs = f.read()

    # Verify that all messages are logged
    assert "Info message" in logs
    assert "Debug message" in logs
    assert "Error message" in logs

def test_logging_format(test_logger):
    logger, log_file = test_logger

    logger.info("Test log format")
    with open(log_file, "r") as f:
        log_line = f.readline()

    # Verify timestamp, log level, and message are in the correct format
    assert "INFO" in log_line
    assert "Test log format" in log_line
