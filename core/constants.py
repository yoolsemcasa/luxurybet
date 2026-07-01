from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

LOGS_DIR = ROOT_DIR / "logs"

DATABASE_DIR = ROOT_DIR / "database"

UPDATE_STATUS = "ONLINE"

DEFAULT_INTERVAL = 5