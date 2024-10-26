'''
This script is for moving files to specific folder. Folders like `Downloads`
are messy as all files are downloaded there.

Save this script in folder where you want to organinze files then run the script.
Then All Set.
'''

import os
import shutil

def create_folder(path, exist_ok=True):
    """Create a directory if it doesn't exist."""
    os.makedirs(path, exist_ok=exist_ok)

def move_file(file_path, target_directory):
    """Move a file to the target directory."""
    try:
        shutil.move(file_path, target_directory)
        print(f"Moved: {file_path} to {target_directory}")
    except Exception as e:
        print(f"Error moving {file_path}: {e}")

def organize_files():
    # Define target directories
    folder_names = ['images', 'documents', 'videos', 'audio', 'archives', 'executables', 'others']
    
    # Create folders in the current working directory
    for folder in folder_names:
        create_folder(folder)

    # Define target directories with their corresponding extensions
    extensions_mapping = {
        'images': ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.heif', '.raw'),
        'documents': ('.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.odt', '.rtf'),
        'videos': ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.mpeg', '.webm'),
        'audio': ('.mp3', '.wav', '.aac', '.ogg', '.flac', '.m4a', '.wma'),
        'archives': ('.zip', '.rar', '.tar', '.gz', '.7z', '.iso'),
        'executables': ('.exe', '.msi', '.app', '.bat', '.sh')
    }

    # Get the current working directory
    current_directory = os.getcwd()

    # Iterate over files in the current directory
    for filename in os.listdir(current_directory):
        # Construct full file path
        file_path = os.path.join(current_directory, filename)

        # Skip the script file itself
        if filename == 'clear_clutter.py':
            continue

        # Check if it's a file
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in extensions_mapping.items():
                if filename.lower().endswith(extensions):
                    move_file(file_path, folder)  # Move to the folder created in the current directory
                    moved = True
                    break
            
            if not moved:
                move_file(file_path, 'others')  # Move to 'others' if no match found

# Organize the files in the current directory
organize_files()
