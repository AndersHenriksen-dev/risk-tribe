from utils.logging import (
    get_logger,
    log_function_execution,
    setup_logging,
)

logger = get_logger(__name__)

@log_function_execution
def main():

    setup_logging("")

    log = get_logger(__name__)

    log.info("Server started.")
    log.debug("Debugging connection issue...")
    log.warning("Low disk space.")
    log.error("Failed to save file!")


if __name__ == "__main__":
    main()
