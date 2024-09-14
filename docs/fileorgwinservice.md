# File Organization Windows Service

## Overview

The `fileorgwinservice.py` script sets up a Windows service to automate the execution of a file organization script (`organize.py`). The service periodically runs the file organization script and logs the output and errors to a specified log file.

## Features

- Automatically executes the file organization script as a Windows service.
- Logs script execution details, including output and errors.
- Handles service start, stop, and management.

## Setup Instructions

1. **Install Python**: Ensure Python is installed on your system.

2. **Install Required Packages**: Install the `pywin32` package, which is required to create and manage Windows services. You can install it using pip:
   ```bash
   pip install pywin32
   ```

3. **Create and Configure `.env` File**:
   - Create a `.env` file in the same directory as `fileorgwinservice.py`.
   - Add the following environment variables to the `.env` file:
     ```env
     SCRIPT_PATH=C:/path/to/your/organize.py
     LOG_FILE=C:/path/to/your/service.log
     ```
   - Ensure that `SCRIPT_PATH` points to the file organization script and `LOG_FILE` points to the log file where the service will write its logs.

4. **Install the Service**:
   - Open a command prompt with administrative privileges.
   - Navigate to the directory containing `fileorgwinservice.py`.
   - Run the following command to install the service:
     ```bash
     python fileorgwinservice.py install
     ```

5. **Start the Service**:
   - After installing the service, start it using the following command:
     ```bash
     python fileorgwinservice.py start
     ```

## Management Commands

- **Start Service**:
  ```bash
  python fileorgwinservice.py start
  ```

- **Stop Service**:
  ```bash
  python fileorgwinservice.py stop
  ```

- **Remove Service**:
  ```bash
  python fileorgwinservice.py remove
  ```

## Error Handling

- **Missing Environment Variables**:
  - If required environment variables (`SCRIPT_PATH` or `LOG_FILE`) are not set, the script will raise a `ValueError`. Ensure that the `.env` file is correctly configured.

- **Script Execution Failures**:
  - Any errors encountered while running the file organization script will be logged to the log file specified in `LOG_FILE`. Check the log file for detailed error messages and script output.

## Logging

- **Log File**:
  - The service logs its activities to the file specified by the `LOG_FILE` environment variable. The log file will include details of the script execution, including output and any errors encountered.

## Troubleshooting

- **Service Not Starting**:
  - Ensure that Python and `pywin32` are correctly installed.
  - Verify that the `.env` file is properly configured and located in the same directory as `fileorgwinservice.py`.
  - Check the log file for any error messages related to service startup.

- **Script Execution Issues**:
  - Review the log file for errors related to the file organization script.
  - Ensure that the file paths and configurations specified in the `.env` file and `organize.py` are correct.
