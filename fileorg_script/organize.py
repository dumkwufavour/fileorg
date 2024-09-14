# import os
# import shutil
# import json
# import logging
# from datetime import datetime
# from pathlib import Path

# # Load configuration from config.json
# with open('config.json', 'r') as config_file:
#     config = json.load(config_file)

# CATEGORIES = config['categories']
# DATE_BASED = config['date_based']
# BACKUP_ENABLED = config['backup_enabled']
# DRY_RUN = config['dry_run']
# VERBOSE = config['verbose']
# OVERWRITE_FILES = config['overwrite_files']

# # Define the source directory
# SOURCE_DIR = Path("")
# # Define the base directory for organized files
# BASE_DEST_DIR = Path("")
# BACKUP_DIR = BASE_DEST_DIR / "backup"

# # Logging configuration
# logging.basicConfig(filename='organizer.log', level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# def organize_file(file_path):
#     """Organizes a single file."""
#     ext = file_path.suffix.lower()
#     for category, extensions in CATEGORIES.items():
#         if ext in extensions:
#             destination_folder = BASE_DEST_DIR / category
#             if DATE_BASED:
#                 date_folder = datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d')
#                 destination_folder = destination_folder / date_folder
#             destination_folder.mkdir(parents=True, exist_ok=True)
#             move_file(file_path, destination_folder)
#             return True
#     logging.warning(f"No category found for {file_path.name}")
#     return False

# def move_file(file_path, destination_folder):
#     """Moves or renames files based on options set in the config."""
#     destination_path = destination_folder / file_path.name
    
#     # Handle duplicate files
#     if destination_path.exists() and not OVERWRITE_FILES:
#         destination_path = handle_duplicates(destination_path)
    
#     if DRY_RUN:
#         print(f"Would move {file_path} to {destination_path}")
#     else:
#         # Backup original file
#         if BACKUP_ENABLED:
#             backup_file(file_path)
        
#         shutil.move(str(file_path), str(destination_path))
#         logging.info(f"Moved {file_path} to {destination_path}")
        
#         if VERBOSE:
#             print(f"Moved {file_path} to {destination_path}")

# def handle_duplicates(destination_path):
#     """Handles duplicate file names by renaming."""
#     counter = 1
#     new_destination_path = destination_path
#     while new_destination_path.exists():
#         new_destination_path = destination_path.with_stem(f"{destination_path.stem}({counter})")
#         counter += 1
#     return new_destination_path

# def backup_file(file_path):
#     """Creates a backup of the original file."""
#     backup_folder = BACKUP_DIR / file_path.parent.name
#     backup_folder.mkdir(parents=True, exist_ok=True)
#     shutil.copy(file_path, backup_folder)
#     logging.info(f"Backed up {file_path} to {backup_folder}")
    
#     if VERBOSE:
#         print(f"Backed up {file_path} to {backup_folder}")

# def organize_directory(directory):
#     """Organizes all files in the directory."""
#     for file_path in Path(directory).iterdir():
#         if file_path.is_file():
#             organized = organize_file(file_path)
#             if not organized:
#                 print(f"Skipping {file_path.name}, no matching category found.")

# def schedule_organization():
#     """Schedule the organization at regular intervals (e.g., daily)."""
#     import schedule
#     import time
    
#     schedule.every().day.at("10:00").do(organize_directory, SOURCE_DIR)
    
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# if __name__ == '__main__':
#     organize_directory(SOURCE_DIR)
    
#     # Uncomment the next line to enable scheduled execution
#     schedule_organization()


# import os
# import shutil
# import json
# import logging
# import csv
# from datetime import datetime
# from pathlib import Path

# # Load configuration from config.json
# with open('config.json', 'r') as config_file:
#     config = json.load(config_file)

# CATEGORIES = config['categories']
# DATE_BASED = config['date_based']
# BACKUP_ENABLED = config['backup_enabled']
# DRY_RUN = config['dry_run']
# VERBOSE = config['verbose']
# OVERWRITE_FILES = config['overwrite_files']

# # Define the source directory
# SOURCE_DIR = Path("")
# # Define the base directory for organized files
# BASE_DEST_DIR = Path("C:/Users/Favourite/Downloads/Organized")
# BACKUP_DIR = BASE_DEST_DIR / "backup"
# # CSV file for logging all operations
# LOG_CSV = BASE_DEST_DIR / "organizer_log.csv"

# # Logging configuration
# logging.basicConfig(filename='organizer.log', level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# def log_to_csv(date_time, description, operation):
#     """Logs actions to a CSV file."""
#     with open(LOG_CSV, mode='a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([date_time, description, operation])

# def custom_log(level, message):
#     """Logs to both the organizer.log file and the CSV file."""
#     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     logging.log(level, message)
    
#     description = logging.getLevelName(level)
#     log_to_csv(now, description, message)

# def organize_file(file_path):
#     """Organizes a single file."""
#     ext = file_path.suffix.lower()
#     for category, extensions in CATEGORIES.items():
#         if ext in extensions:
#             destination_folder = BASE_DEST_DIR / category
#             if DATE_BASED:
#                 date_folder = datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d')
#                 destination_folder = destination_folder / date_folder
#             destination_folder.mkdir(parents=True, exist_ok=True)
#             move_file(file_path, destination_folder)
#             return True
#     # If no matching category is found, log the unmatched extension
#     warning_message = f"No category found for {file_path.name}"
#     custom_log(logging.WARNING, warning_message)
#     return False

# def move_file(file_path, destination_folder):
#     """Moves or renames files based on options set in the config."""
#     destination_path = destination_folder / file_path.name
    
#     # Handle duplicate files
#     if destination_path.exists() and not OVERWRITE_FILES:
#         destination_path = handle_duplicates(destination_path)
    
#     if DRY_RUN:
#         print(f"Would move {file_path} to {destination_path}")
#     else:
#         # Backup original file
#         if BACKUP_ENABLED:
#             backup_file(file_path)
        
#         shutil.move(str(file_path), str(destination_path))
#         info_message = f"Moved {file_path} to {destination_path}"
#         custom_log(logging.INFO, info_message)
        
#         if VERBOSE:
#             print(info_message)

# def handle_duplicates(destination_path):
#     """Handles duplicate file names by renaming."""
#     counter = 1
#     new_destination_path = destination_path
#     while new_destination_path.exists():
#         new_destination_path = destination_path.with_stem(f"{destination_path.stem}({counter})")
#         counter += 1
#     return new_destination_path

# def backup_file(file_path):
#     """Creates a backup of the original file."""
#     backup_folder = BACKUP_DIR / file_path.parent.name
#     backup_folder.mkdir(parents=True, exist_ok=True)
#     shutil.copy(file_path, backup_folder)
#     info_message = f"Backed up {file_path} to {backup_folder}"
#     custom_log(logging.INFO, info_message)
    
#     if VERBOSE:
#         print(info_message)

# def organize_directory(directory):
#     """Organizes all files in the directory."""
#     for file_path in Path(directory).iterdir():
#         if file_path.is_file():
#             organized = organize_file(file_path)
#             if not organized:
#                 print(f"Skipping {file_path.name}, no matching category found.")

# def schedule_organization():
#     """Schedule the organization at regular intervals (e.g., daily)."""
#     import schedule
#     import time
    
#     schedule.every().day.at("10:00").do(organize_directory, SOURCE_DIR)
    
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# if __name__ == '__main__':
#     # Create the CSV file with a header if it doesn't exist
#     if not LOG_CSV.exists():
#         with open(LOG_CSV, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["Date-Time", "Description", "Operation"])
    
#     organize_directory(SOURCE_DIR)
    
#     # Uncomment the next line to enable scheduled execution
#     schedule_organization()



import os
import shutil
import json
import logging
import csv
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import sys

# Load environment variables from .env file
load_dotenv()

# Retrieve file paths and configuration from environment variables
config_path = os.getenv('CONFIG_PATH')
source_dir = os.getenv('SOURCE_DIR')
base_dest_dir = os.getenv('BASE_DEST_DIR')
log_csv = os.getenv('LOG_CSV')

# Ensure required environment variables are loaded
if not all([config_path, source_dir, base_dest_dir, log_csv]):
    raise ValueError("One or more environment variables are missing.")

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

CATEGORIES = config.get('categories', {})
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

# Ensure SOURCE_DIR and BASE_DEST_DIR exist
if not SOURCE_DIR.exists():
    print(f"Source directory does not exist: {SOURCE_DIR}")
    sys.exit(1)

if not BASE_DEST_DIR.exists():
    print(f"Base destination directory does not exist: {BASE_DEST_DIR}")
    sys.exit(1)

# Set up logging to both log file and CSV
def setup_logging():
    """Sets up logging to both the organizer.log and the CSV file."""
    logging.basicConfig(filename='organizer.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

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
    description = logging.getLevelName(level)
    log_to_csv(date_time, description, message)

def organize_file(file_path):
    """Organizes a single file."""
    ext = file_path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            destination_folder = BASE_DEST_DIR / category
            if DATE_BASED:
                date_folder = datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d')
                destination_folder = destination_folder / date_folder
            destination_folder.mkdir(parents=True, exist_ok=True)
            move_file(file_path, destination_folder)
            return True
    warning_message = f"No category found for {file_path.name}"
    log_message(logging.WARNING, warning_message)
    return False

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

def handle_duplicates(destination_path):
    """Handles duplicate file names by renaming."""
    counter = 1
    new_destination_path = destination_path
    while new_destination_path.exists():
        new_destination_path = destination_path.with_stem(f"{destination_path.stem}({counter})")
        counter += 1
    return new_destination_path

def backup_file(file_path):
    """Creates a backup of the original file."""
    backup_folder = BACKUP_DIR / file_path.parent.name
    backup_folder.mkdir(parents=True, exist_ok=True)
    shutil.copy(file_path, backup_folder)
    info_message = f"Backed up {file_path} to {backup_folder}"
    log_message(logging.INFO, info_message)
    
    if VERBOSE:
        print(info_message)

def organize_directory(directory):
    """Organizes all files in the directory."""
    print(f"Starting organization of files in {directory}...")
    for file_path in Path(directory).iterdir():
        if file_path.is_file():
            organized = organize_file(file_path)
            if not organized:
                print(f"Skipping {file_path.name}, no matching category found.")
    print(f"Completed organization of files in {directory}.")

def schedule_organization():
    """Schedule the organization at regular intervals (e.g., daily)."""
    import schedule
    import time
    
    def task():
        print("Starting scheduled organization...")
        log_message(logging.INFO, "Scheduled organization task started.")
        organize_directory(SOURCE_DIR)
        print("Scheduled organization completed.")
        log_message(logging.INFO, "Scheduled organization task completed.")
    
    schedule.every().day.at("12:03").do(task)
    
    print("Scheduler started. Waiting for the next scheduled task.")
    log_message(logging.INFO, "Scheduler started.")

    while True:
        next_run = schedule.next_run()
        next_run_time = next_run.strftime("%Y-%m-%d %H:%M:%S") if next_run else "N/A"
        print(f"Next scheduled task at: {next_run_time}")
        
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    setup_logging()
    
    try:
        organize_directory(SOURCE_DIR)
        # Uncomment the next line to enable scheduled execution
        schedule_organization()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting gracefully...")
        log_message(logging.INFO, "Process interrupted by user.")