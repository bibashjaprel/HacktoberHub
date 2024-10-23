import os
import shutil
import datetime
import logging
from pathlib import Path
import zipfile

class BackupManager:
    def __init__(self, source_dirs, backup_dir):
        """
        Initialize the backup manager.
        
        Args:
            source_dirs (list): List of directory paths to backup
            backup_dir (str): Directory where backups will be stored
        """
        self.source_dirs = source_dirs
        self.backup_dir = backup_dir
        self.timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            handlers=[
                logging.FileHandler(f'backup_{self.timestamp}.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def create_backup_dir(self):
        """Create the backup directory if it doesn't exist."""
        try:
            os.makedirs(self.backup_dir, exist_ok=True)
            self.logger.info(f"Backup directory created/verified: {self.backup_dir}")
        except Exception as e:
            self.logger.error(f"Error creating backup directory: {e}")
            raise
            
    def compress_directory(self, source_dir):
        """
        Compress a directory into a ZIP file with timestamp.
        
        Args:
            source_dir (str): Directory to compress
            
        Returns:
            str: Path to the created ZIP file
        """
        try:
            # Create zip filename with timestamp
            dir_name = os.path.basename(source_dir)
            zip_filename = f"{dir_name}_{self.timestamp}.zip"
            zip_path = os.path.join(self.backup_dir, zip_filename)
            
            # Create ZIP file
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(source_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, source_dir)
                        zipf.write(file_path, arcname)
                        
            self.logger.info(f"Successfully compressed {source_dir} to {zip_path}")
            return zip_path
        except Exception as e:
            self.logger.error(f"Error compressing directory {source_dir}: {e}")
            raise
            
    def run_backup(self):
        """Execute the backup process for all source directories."""
        try:
            self.create_backup_dir()
            
            for source_dir in self.source_dirs:
                if not os.path.exists(source_dir):
                    self.logger.warning(f"Source directory does not exist: {source_dir}")
                    continue
                    
                self.logger.info(f"Starting backup of: {source_dir}")
                zip_path = self.compress_directory(source_dir)
                self.logger.info(f"Backup completed: {zip_path}")
                
        except Exception as e:
            self.logger.error(f"Backup process failed: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    source_directories = [
        "/path/to/first/directory",
        "/path/to/second/directory"
    ]
    backup_directory = "/path/to/backup/location"
    
    backup_manager = BackupManager(source_directories, backup_directory)
    backup_manager.run_backup()