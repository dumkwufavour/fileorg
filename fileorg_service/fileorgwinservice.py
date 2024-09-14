import win32serviceutil
import win32service
import win32event
import win32api
import win32evtlogutil
import win32evtlog
import logging
import logging.handlers
import os
import subprocess
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve paths from environment variables
SCRIPT_PATH = os.getenv('SCRIPT_PATH')
LOG_FILE = os.getenv('LOG_FILE')

# Ensure required environment variables are loaded
if not SCRIPT_PATH or not LOG_FILE:
    raise ValueError("One or more environment variables are missing.")

class FileOrgService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'FileOrgService'
    _svc_display_name_ = 'File Organization Service'
    _svc_description_ = 'A service to organize files in a specified directory'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.setup_logging()
        self.is_running = True

    def setup_logging(self):
        """Set up detailed logging."""
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # File handler for service logs
        file_handler = logging.handlers.RotatingFileHandler(
            LOG_FILE, maxBytes=10*1024*1024, backupCount=5
        )
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def main(self):
        """Main method for the service."""
        self.logger.info('Service is starting.')
        while self.is_running:
            self.logger.info('Service is running...')
            
            # Run your script (using subprocess)
            try:
                result = subprocess.run(
                    ['python', SCRIPT_PATH], 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE
                )
                self.logger.info(f"Script output: {result.stdout.decode()}")
                if result.stderr:
                    self.logger.error(f"Script error: {result.stderr.decode()}")
            except Exception as e:
                self.logger.error(f"Failed to run script: {e}")
            
            win32event.WaitForSingleObject(self.hWaitStop, 5000)
        
        self.logger.info('Service is stopping.')

    def SvcDoRun(self):
        """Run method for the service."""
        self.logger.info('Service is starting...')
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        self.main()

    def SvcStop(self):
        """Stop method for the service."""
        self.logger.info('Service is stopping...')
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.is_running = False
        win32event.SetEvent(self.hWaitStop)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(FileOrgService)