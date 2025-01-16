# File Organization Script

## Overview

The `organize.py` script automates file organization by categorizing files in a directory based on their extensions. It supports backing up files, resolving duplicate names, and providing a preview mode for planned actions. Additionally, it can be scheduled to run automatically at specified intervals. The script is fully cross-platform and works seamlessly on Windows, macOS, and Linux.

## Features

- Cross-platform support for Windows, macOS, and Linux.
- Categorizes files based on their extensions using customizable rules.
- Creates backups of files before organizing them (optional).
- Renames files to avoid overwriting duplicates.
- Supports a dry run mode to preview actions without making changes.
- Multi-threaded file organization for improved performance.
- Logs activities to both a log file and a CSV file.
- Configurable scheduling to automate file organization tasks.

## Setup Instructions

### 1. Install Python and Required Packages
Ensure Python is installed, and then install the required libraries:
```bash
pip install python-dotenv schedule
```

### 2. Create and Configure `.env` File
Create a `.env` file in the script's directory with the following environment variables:
```env
CONFIG_PATH=/path/to/config.json
SOURCE_DIR=/path/to/source/directory
BASE_DEST_DIR=/path/to/destination/directory
LOG_CSV=/path/to/log.csv
SCHEDULE_TIME=12:03
```
- Replace paths with your specific file locations.
- Use forward slashes (`/`) for compatibility across platforms.
- Adjust `SCHEDULE_TIME` (in 24-hour format) for the scheduling feature.

### 3. Create and Configure `config.json`
Create a `config.json` file at the location specified by `CONFIG_PATH`. Use the following template:
```json
{
  "categories": {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv"]
  },
  "date_based": true,
  "backup_enabled": true,
  "dry_run": false,
  "verbose": true,
  "overwrite_files": false
}
```
- Customize the categories and file extensions.
- Adjust the other configuration settings as needed.

### 4. Run the Script
Run the script manually using:
```bash
python organize.py
```

## Usage

### Organize Files
The script organizes files from `SOURCE_DIR` into categories defined in `config.json` and places them in `BASE_DEST_DIR`. If `date_based` is enabled, files are further organized into subdirectories by modification date.

### Backup Files
If `backup_enabled` is set to `true`, files are backed up to a `backup` directory inside `BASE_DEST_DIR` before being moved.

### Dry Run Mode
If `dry_run` is `true`, the script only previews its actions without making changes.

### Verbose Mode
If `verbose` is `true`, detailed information about operations is displayed in the console.

### Handling Duplicates
If `overwrite_files` is `false`, duplicate files are renamed with a counter (e.g., `file(1).txt`).

### Scheduling
To automate organization tasks:
1. Uncomment the scheduling section in the script.
2. The script will run daily at the time specified by `SCHEDULE_TIME`.

## Logging

- **Log File**: Logs detailed activity in `organizer.log`.
- **CSV Log**: Logs activity in a CSV file specified by `LOG_CSV`, including timestamps, descriptions, and actions.

## Error Handling

- **Missing Environment Variables**: The script raises a `ValueError` if required variables are missing.
- **Invalid Configurations**: The script exits with an error if `config.json` is not found or contains invalid JSON.
- **Directory Errors**: If the source or destination directories are missing, the script exits with an error message.

## Troubleshooting

- **Script Not Running**: Ensure the `.env` and `config.json` files are properly set up and paths are valid.
- **Organization Issues**: Check `organizer.log` and `LOG_CSV` for details about any problems.
- **Backup Redundancy**: The script skips redundant backups by comparing file checksums.