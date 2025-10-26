import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Create logs directory
LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

# --- Custom formatter for console ---
class ConsoleFormatter(logging.Formatter):
    """Simplified and colored log output for console."""

    COLORS = {
        'DEBUG': '\033[90m',    # grey
        'INFO': '\033[94m',     # blue
        'WARNING': '\033[93m',  # yellow
        'ERROR': '\033[91m',    # red
        'CRITICAL': '\033[95m', # magenta
        'RESET': '\033[0m'
    }

    def format(self, record):
        color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        message = super().format(record)
        return f"{color}{message}{self.COLORS['RESET']}"

# --- Console handler (print-like) ---
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = ConsoleFormatter("%(message)s")
console_handler.setFormatter(console_formatter)

# --- File handler (detailed logging) ---
file_handler = RotatingFileHandler(LOG_FILE, maxBytes=5_000_000, backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)

# --- Root logger setup ---
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Optional: disable noisy logs from external libs
logging.getLogger("urllib3").setLevel(logging.WARNING)

def get_logger(name: str = None):
    """Return a named logger."""
    return logging.getLogger(name)
