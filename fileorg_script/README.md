# File Organization Script

## Overview
This script organizes files in a specified directory based on the configuration in `config.json`.

## Configuration
- **CONFIG_PATH**: Path to the configuration file.
- **SOURCE_DIR**: Directory to scan for files.
- **BASE_DEST_DIR**: Directory where files will be organized.
- **LOG_CSV**: Path to the CSV log file.

## Usage
- To run the script manually: `python organize.py`

## Features
- Organizes files into categories based on file extensions.
- Optionally backs up files.
- Can handle duplicate file names.
