# File Organization Script

## Overview

The `organize.py` script organizes files in a specified directory based on configuration settings. It supports categorizing files, backing up files, handling duplicate file names, and optionally running in a dry run mode. The script can also be scheduled to run at regular intervals.

## Features

- Organizes files into categories based on their extensions.
- Optionally backs up files before moving them.
- Handles duplicate file names by renaming.
- Supports dry run mode to preview actions without making changes.
- Allows scheduling of file organization tasks.
- Logs activities to a log file and a CSV file.

## Setup Instructions

1. **Install Python and Required Packages**:
   - Ensure Python is installed on your system.
   - Install the `python-dotenv` and `schedule` packages using pip:
     ```bash
     pip install python-dotenv schedule
     ```

2. **Create and Configure `.env` File**:
   - Create a `.env` file in the same directory as `organize.py`.
   - Add the following environment variables to the `.env` file:
     ```env
     CONFIG_PATH=C:/path/to/your/config.json
     SOURCE_DIR=C:/path/to/source/directory
     BASE_DEST_DIR=C:/path/to/destination/directory
     LOG_CSV=C:/path/to/your/log.csv
     ```

3. **Create and Configure `config.json`**:
   - Create a `config.json` file in the path specified by `CONFIG_PATH`.
   - Add the following configuration settings:
     ```json
     {
       "categories": {
         "Category1": [".ext1", ".ext2"],
         "Category2": [".ext3"]
       },
       "date_based": false,
       "backup_enabled": true,
       "dry_run": false,
       "verbose": true,
       "overwrite_files": false
     }
     ```
   - Replace the values with your specific configuration for file categories and behavior.

4. **Run the Script**:
   - You can run the script manually using the following command:
     ```bash
     python organize.py
     ```

## Usage

- **Organize Files**:
  - The script will organize files from the `SOURCE_DIR` into categories defined in `config.json` and place them in the `BASE_DEST_DIR`.

- **Backup Files**:
  - If `backup_enabled` is set to `true` in `config.json`, the script will back up files before moving them.

- **Dry Run**:
  - If `dry_run` is set to `true`, the script will only print the actions it would take without making any changes.

- **Verbose Mode**:
  - If `verbose` is set to `true`, the script will print additional information about its operations to the console.

- **Handle Duplicates**:
  - If a file with the same name already exists in the destination directory and `overwrite_files` is set to `false`, the script will rename the file to avoid overwriting.

- **Scheduling**:
  - The script can be scheduled to run at regular intervals using the `schedule` library. The default configuration schedules the script to run daily at 12:03 PM. To change the schedule, modify the `schedule.every().day.at("12:03").do(task)` line in the `schedule_organization` function.

## Logging

- **Log File**:
  - The script logs its activities to `organizer.log`, including details of file movements and backups.

- **CSV Log**:
  - The script also logs activities to a CSV file specified by `LOG_CSV`. The CSV file includes timestamps, descriptions, and operations.

## Error Handling

- **Missing Environment Variables**:
  - The script will raise a `ValueError` if any required environment variables are missing. Ensure that the `.env` file is correctly configured.

- **Configuration File Issues**:
  - The script will exit with an error message if the `config.json` file is not found or contains invalid JSON.

- **Directory Issues**:
  - The script will exit with an error message if the source or destination directories do not exist.

## Troubleshooting

- **Script Not Running**:
  - Verify that all environment variables in the `.env` file are correctly set.
  - Ensure that the `config.json` file exists and is properly formatted.
  - Check the log file and CSV file for any errors or warnings.

- **File Organization Issues**:
  - Review the `organizer.log` and `LOG_CSV` files for detailed information on any issues encountered during file organization.
