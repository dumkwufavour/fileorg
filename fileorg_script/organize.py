import os
import shutil
import json
import logging
import csv
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import sys
from concurrent.futures import ThreadPoolExecutor
import hashlib
import schedule
import time

# Load environment variables from .env file
load_dotenv()

# Retrieve file paths and configuration from environment variables
config_path = os.getenv('CONFIG_PATH', './config.json')
source_dir = os.getenv('SOURCE_DIR', './source')
base_dest_dir = os.getenv('BASE_DEST_DIR', './destination')
log_csv = os.getenv('LOG_CSV', './log.csv')
schedule_time = os.getenv('SCHEDULE_TIME', '12:03')

# Validate required environment variables
if not all([config_path, source_dir, base_dest_dir, log_csv]):
    raise ValueError("Environment variables 'CONFIG_PATH', 'SOURCE_DIR', 'BASE_DEST_DIR', and 'LOG_CSV' are required.")

# Load configuration from config.json
try:
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    print(f"Configuration file not found: {config_path}")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"Error decoding JSON from configuration file: {config_path}")
    sys.exit(1)

# Configuration parameters
CATEGORIES = config.get('categories', {})
if not isinstance(CATEGORIES, dict):
    raise ValueError("'categories' in config must be a dictionary of {category: [extensions]}.")

DATE_BASED = config.get('date_based', False)
BACKUP_ENABLED = config.get('backup_enabled', False)
DRY_RUN = config.get('dry_run', False)
VERBOSE = config.get('verbose', False)
OVERWRITE_FILES = config.get('overwrite_files', False)

# Define directories and file paths
SOURCE_DIR = Path(source_dir)
BASE_DEST_DIR = Path(base_dest_dir)
BACKUP_DIR = BASE_DEST_DIR / "backup"
LOG_CSV = Path(log_csv)

# Ensure directories exist
for directory in [SOURCE_DIR, BASE_DEST_DIR]:
    if not directory.exists():
        print(f"Directory does not exist: {directory}")
        sys.exit(1)

# Setup logging
def setup_logging():
    """Sets up logging to both log file and CSV file."""
    logging.basicConfig(
        filename='organizer.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    if not LOG_CSV.exists():
        with open(LOG_CSV, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date-Time", "Description", "Operation"])

def log_to_csv(date_time, description, operation):
    """Logs actions to a CSV file."""
    with open(LOG_CSV, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date_time, description, operation])

def log_message(level, message):
    """Logs a message to both the log file and CSV file."""
    logging.log(level, message)
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_to_csv(date_time, logging.getLevelName(level), message)

def file_checksum(file_path):
    """Generates an MD5 checksum for a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def backup_file(file_path):
    """Creates a backup of the original file."""
    backup_folder = BACKUP_DIR / file_path.parent.name
    backup_folder.mkdir(parents=True, exist_ok=True)
    backup_path = backup_folder / file_path.name

    if backup_path.exists() and file_checksum(file_path) == file_checksum(backup_path):
        info_message = f"Backup skipped for {file_path}: identical file exists."
    else:
        shutil.copy(file_path, backup_path)
        info_message = f"Backed up {file_path} to {backup_folder}"

    log_message(logging.INFO, info_message)
    if VERBOSE:
        print(info_message)

def handle_duplicates(destination_path):
    """Handles duplicate file names by renaming."""
    counter = 1
    new_destination_path = destination_path
    while new_destination_path.exists():
        new_destination_path = destination_path.with_stem(f"{destination_path.stem}({counter})")
        counter += 1
    return new_destination_path

def move_file(file_path, destination_folder):
    """Moves or renames files based on options set in the config."""
    destination_path = destination_folder / file_path.name

    if destination_path.exists() and not OVERWRITE_FILES:
        destination_path = handle_duplicates(destination_path)

    if DRY_RUN:
        print(f"Would move {file_path} to {destination_path}")
    else:
        if BACKUP_ENABLED:
            backup_file(file_path)
        shutil.move(str(file_path), str(destination_path))
        info_message = f"Moved {file_path} to {destination_path}"
        log_message(logging.INFO, info_message)
        if VERBOSE:
            print(info_message)

def organize_file(file_path):
    """Organizes a single file."""
    ext = file_path.suffix.lower()
    category = next((cat for cat, exts in CATEGORIES.items() if ext in exts), None)
    if category:
        destination_folder = BASE_DEST_DIR / category
        if DATE_BASED:
            date_folder = datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d')
            destination_folder = destination_folder / date_folder
        try:
            destination_folder.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            log_message(logging.ERROR, f"Failed to create directory {destination_folder}: {e}")
            return False
        move_file(file_path, destination_folder)
        return True
    else:
        log_message(logging.WARNING, f"No category found for {file_path.name}")
        return False

def organize_directory(directory):
    """Organizes all files in the directory."""
    print(f"Starting organization of files in {directory}...")
    file_paths = [file for file in Path(directory).iterdir() if file.is_file()]
    with ThreadPoolExecutor() as executor:
        executor.map(organize_file, file_paths)
    print(f"Completed organization of files in {directory}.")

def schedule_organization():
    """Schedule the organization at regular intervals."""
    def task():
        print("Starting scheduled organization...")
        log_message(logging.INFO, "Scheduled organization task started.")
        organize_directory(SOURCE_DIR)
        print("Scheduled organization completed.")
        log_message(logging.INFO, "Scheduled organization task completed.")

    schedule.every().day.at(schedule_time).do(task)

    print("Scheduler started. Waiting for the next scheduled task.")
    log_message(logging.INFO, "Scheduler started.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    setup_logging()
    try:
        organize_directory(SOURCE_DIR)
        # Uncomment the next line to enable scheduling
        # schedule_organization()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting gracefully...")
        log_message(logging.INFO, "Process interrupted by user.")
