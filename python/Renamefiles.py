import os
import glob

def bulk_rename_files(folder_path, new_name, file_extension):
    files = glob.glob(os.path.join(folder_path, f"*.{file_extension}"))
    
    if not files:
        print(f"No files with .{file_extension} extension found in the folder.")
        return

    for index, file_path in enumerate(files):
        old_file_name = os.path.basename(file_path)
        
        new_file_name = f"{new_name}_{index + 1}.{file_extension}"
        
        new_file_path = os.path.join(folder_path, new_file_name)
        
        os.rename(file_path, new_file_path)
        
        print(f"Renamed '{old_file_name}' to '{new_file_name}'")

folder_path = input("Enter the folder path: ")  # Example: C:/path/to/your/folder
new_name = input("Enter the new base name for files: ")  # Example: NewFileName
file_extension = input("Enter the file extension (e.g., txt, jpg): ")  # Example: txt

bulk_rename_files(folder_path, new_name, file_extension)
