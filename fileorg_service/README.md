# File Organization Windows Service

## Overview
This script sets up a Windows service that runs the file organization script (`organize.py`).

## Setup
1. **Dependencies**: Ensure `pywin32` is installed.
2. **Configuration**:
   - Set up the `.env` file with the `SCRIPT_PATH` and `LOG_FILE` paths.
3. **Installation**:
   - Run `python fileorgwinservice.py install` to install the service.
   - Run `python fileorgwinservice.py start` to start the service.

## Management
- **Stop Service**: `python fileorgwinservice.py stop`
- **Remove Service**: `python fileorgwinservice.py remove`
