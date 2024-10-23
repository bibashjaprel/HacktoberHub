# Automated Backup Script

A Python script that automatically backs up specified directories, compresses them with timestamps, and maintains logs of the backup process.

## Features

- Automated backup of multiple directories
- ZIP compression with timestamps
- Detailed logging of backup operations
- Error handling and reporting
- Cross-platform compatibility

## Requirements

- Python 3.6 or higher
- No additional external dependencies required

## Installation

1. Clone or download this repository:
```bash
git clone https://github.com/yourusername/backup-script.git
cd backup-script
```

2. Make sure you have Python 3.6+ installed:
```bash
python --version
```

## Configuration

Edit the script to specify your source and backup directories:

```python
source_directories = [
    "/path/to/first/directory",
    "/path/to/second/directory"
]
backup_directory = "/path/to/backup/location"
```

Replace the paths with your actual directory paths.

## Usage

1. Basic usage:
```bash
python backup_script.py
```

2. Using as a module in your own code:
```python
from backup_script import BackupManager

backup_manager = BackupManager(
    source_dirs=["/path/to/backup"],
    backup_dir="/path/to/store/backups"
)
backup_manager.run_backup()
```

## Output

The script will:
1. Create timestamped ZIP files for each backed-up directory
2. Generate a log file (`backup_YYYYMMDD_HHMMSS.log`) with details of the backup process

## File Naming Convention

Backup files are named using the following format:
`directoryname_YYYYMMDD_HHMMSS.zip`

Example: `documents_20240223_143022.zip`

## Logging

The script creates detailed logs including:
- Backup start and completion times
- Success/failure status for each operation
- Error messages if any issues occur

Logs are saved both to a file and displayed in the console.

## Error Handling

The script includes comprehensive error handling for:
- Invalid source directories
- Insufficient permissions
- Disk space issues
- File access problems

## Contributing

Feel free to submit issues and enhancement requests!


