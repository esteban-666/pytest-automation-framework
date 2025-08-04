"""
Logging utility for the automation framework.
"""

import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from loguru import logger


class InterceptHandler(logging.Handler):
    """Intercept standard logging and redirect to loguru."""

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def setup_logger(
    level: str = "INFO",
    log_file: Optional[str] = None,
    log_format: str = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    rotation: str = "10 MB",
    retention: str = "30 days",
    compression: str = "zip",
) -> logger:
    """
    Setup and configure the logger.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Path to log file
        log_format: Log message format
        rotation: Log rotation size
        retention: Log retention period
        compression: Log compression format

    Returns:
        Configured logger instance
    """
    # Remove default handler
    logger.remove()

    # Add console handler
    logger.add(
        sys.stdout,
        format=log_format,
        level=level,
        colorize=True,
        backtrace=True,
        diagnose=True,
    )

    # Add file handler if specified
    if log_file:
        # Create logs directory if it doesn't exist
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        logger.add(
            log_file,
            format=log_format,
            level=level,
            rotation=rotation,
            retention=retention,
            compression=compression,
            backtrace=True,
            diagnose=True,
        )

    # Intercept standard logging
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

    # Intercept third-party loggers
    for name in logging.root.manager.loggerDict:
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    return logger


def get_test_logger(name: str = None) -> logger:
    """
    Get a logger instance for test logging.

    Args:
        name: Logger name (usually __name__)

    Returns:
        Logger instance
    """
    if name:
        return logger.bind(name=name)
    return logger


def log_test_start(test_name: str, test_params: dict = None):
    """Log test start information."""
    logger.info(f"🚀 Starting test: {test_name}")
    if test_params:
        logger.debug(f"Test parameters: {test_params}")


def log_test_end(test_name: str, status: str = "PASSED", duration: float = None):
    """Log test end information."""
    if status.upper() == "PASSED":
        logger.info(f"✅ Test completed: {test_name}")
    elif status.upper() == "FAILED":
        logger.error(f"❌ Test failed: {test_name}")
    elif status.upper() == "SKIPPED":
        logger.warning(f"⏭️ Test skipped: {test_name}")

    if duration:
        logger.info(f"⏱️ Test duration: {duration:.2f} seconds")


def log_step(step_name: str, step_details: str = None):
    """Log test step information."""
    logger.info(f"📋 Step: {step_name}")
    if step_details:
        logger.debug(f"Step details: {step_details}")


def log_assertion(
    assertion_name: str,
    expected: Any = None,
    actual: Any = None,
    status: str = "PASSED",
):
    """Log assertion information."""
    if status.upper() == "PASSED":
        logger.info(f"✅ Assertion passed: {assertion_name}")
    else:
        logger.error(f"❌ Assertion failed: {assertion_name}")
        if expected is not None and actual is not None:
            logger.error(f"Expected: {expected}")
            logger.error(f"Actual: {actual}")


def log_api_request(method: str, url: str, headers: dict = None, data: Any = None):
    """Log API request information."""
    logger.info(f"🌐 API Request: {method} {url}")
    if headers:
        logger.debug(f"Headers: {headers}")
    if data:
        logger.debug(f"Data: {data}")


def log_api_response(
    status_code: int, response_data: Any = None, duration: float = None
):
    """Log API response information."""
    if 200 <= status_code < 300:
        logger.info(f"✅ API Response: {status_code}")
    else:
        logger.error(f"❌ API Response: {status_code}")

    if response_data:
        logger.debug(f"Response data: {response_data}")

    if duration:
        logger.info(f"⏱️ API call duration: {duration:.2f} seconds")


def log_web_action(action: str, element_info: str = None, value: Any = None):
    """Log web automation actions."""
    logger.info(f"🖥️ Web Action: {action}")
    if element_info:
        logger.debug(f"Element: {element_info}")
    if value:
        logger.debug(f"Value: {value}")


def log_database_query(query: str, params: dict = None, duration: float = None):
    """Log database query information."""
    logger.info(f"🗄️ Database Query: {query}")
    if params:
        logger.debug(f"Parameters: {params}")
    if duration:
        logger.info(f"⏱️ Query duration: {duration:.2f} seconds")


def log_performance_metric(metric_name: str, value: float, unit: str = "ms"):
    """Log performance metrics."""
    logger.info(f"📊 Performance: {metric_name} = {value} {unit}")


def log_error(error: Exception, context: str = None):
    """Log error information."""
    logger.error(f"💥 Error in {context or 'unknown context'}: {str(error)}")
    logger.exception(error)


def log_warning(message: str, context: str = None):
    """Log warning information."""
    logger.warning(f"⚠️ Warning in {context or 'unknown context'}: {message}")


def log_info(message: str, context: str = None):
    """Log information message."""
    logger.info(f"ℹ️ Info in {context or 'unknown context'}: {message}")


def log_debug(message: str, context: str = None):
    """Log debug message."""
    logger.debug(f"🔍 Debug in {context or 'unknown context'}: {message}")


# Create logs directory
os.makedirs("logs", exist_ok=True)

# Setup default logger
setup_logger(level=os.getenv("LOG_LEVEL", "INFO"), log_file="logs/test.log")
