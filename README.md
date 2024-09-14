# File Organization Project

## Overview
This project includes two main components: a Python script for organizing files and a Windows service to run this script periodically.

## Components
1. **organize.py**: Organizes files based on categories defined in the configuration file.
2. **fileorgwinservice.py**: A Windows service that runs the file organization script.

## Installation and Setup
1. **Install Python**: Ensure Python is installed on your system.
2. **Install Dependencies**: Run `pip install -r requirements.txt` to install necessary packages.
3. **Setup Environment**:
   - Create a `.env` file with the required environment variables.
   - Ensure `config.json` is properly configured.

## Usage
- To run the file organization script manually: `python organize.py`
- To install and start the Windows service: `python fileorgwinservice.py install` and `python fileorgwinservice.py start`
