import logging
import logging.config
import os
from datetime import datetime
import sys
import time
import traceback
from functools import wraps

__tracebackhide__ = True

def format_elapsed_time(start_time, end_time):
    """Format the elapsed time as 'minutes and seconds' or just 'seconds'."""

    elapsed_time = end_time - start_time

    if elapsed_time > 60:
        minutes = int(elapsed_time // 60)
        seconds = elapsed_time % 60
        return f"{minutes} minutes and {seconds:.2f} seconds"

    else:
        return f"{elapsed_time:.2f} seconds"


def raise_custom_exception(e, func_name):
    """Raise a custom exception with additional context."""

    custom_message = f"\nAn error occurred in {func_name}.\n"
    e.add_note(custom_message)  # Add a note to the exception (Python 3.11+ feature)
    raise e

 

def log_function_execution(func):
    """
    A decorator to log the execution of a function, including timing and error handling.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__module__)  # Get logger for the calling module
        func_name = func.__qualname__  # Qualified name includes class if it's a method
        try:
            # Log the start of the function
            logger.info(f"\n\nStarting execution of '{func_name}'...")
            start_time = time.time()

            # Execute the function
            result = func(*args, **kwargs)

            # Measure elapsed time
            end_time = time.time()
            elapsed_time = format_elapsed_time(start_time, end_time)

            # Log successful execution
            logger.info(f"Finished execution of '{func_name}' in {elapsed_time}.\n\n")
            if result is not None:
                logger.debug(f"'{func_name}' returned: {result}")
            return result

        except Exception as e:
            # Log the exception with context
            logger.error(f"An error occurred in '{func_name}': {e}")
            raise_custom_exception(e, func_name)

    return wrapper


def setup_logging(base_path):
    # Get the name of the top-level script (the main entry point)
    script_name = os.path.basename(sys.argv[0]).split('.')[0].upper()

    # Ensure the logs directory exists
    log_dir = os.path.join(base_path, "logs")
    os.makedirs(log_dir, exist_ok=True)

    # Create a dynamic log file name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
    log_file = os.path.join(log_dir, f"{script_name}_{timestamp}.log")

    # Logging configuration
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "detailed": {
                "format": (
                    # "%(filename)s - %(funcName)s() - line %(lineno)d - %(message)s"
                    "%(asctime)s - %(levelname)s - "
                    "%(filename)s( %(funcName)s(), line %(lineno)d) - %(message)s"
                ),
                "datefmt": "%Y-%m-%d %H:%M"  # Custom datetime format
            },

            "simple": {
                # "format": "%(levelname)s: %(filename)s - %(message)s"
                "format": "%(message)s"
            },
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "simple",
                "level": "INFO",
            },

            "file": {
                "class": "logging.FileHandler",
                "formatter": "detailed",
                "filename": log_file,
                "level": "DEBUG",
            },
        },

        "root": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
        },
    }

    # Apply the configuration
    logging.config.dictConfig(logging_config)

    # Print the log file location for convenience
    print(f"Logging to file: {log_file}")

    # Set up sys.excepthook to log unhandled exceptions
    def log_unhandled_exceptions(exc_type, exc_value, exc_traceback):
        logging.critical("Unhandled exception occurred", exc_info=(exc_type, exc_value, exc_traceback))

    sys.excepthook = log_unhandled_exceptions


def get_logger(name):
    """
    Retrieve a logger with the given name.
 
    Args:
        name (str): The name of the logger (usually __name__).

    Returns:
        logging.Logger: A configured logger instance.
    """
    return logging.getLogger(name)