#!/bin/bash

# Function to create and move files to a directory if there are files to move
move_files() {
  local ext="$1" # File extension
  local folder_name="$2" # Folder name

  # Check if there are files with the specified extension
  if ls *."$ext" 1> /dev/null 2>&1; then
    # Check if the folder exists, if not, create it
    if [ ! -d "$folder_name" ]; then
      mkdir "$folder_name"
      echo "Created directory: $folder_name"
    fi

    # Move the files with the specified extension to the folder
    mv *."$ext" "$folder_name" 2>/dev/null
    echo "Moved *.$ext files to $folder_name"
  fi
}

# Organize images
move_files "jpg" "Images"
move_files "jpeg" "Images"
move_files "png" "Images"
move_files "gif" "Images"
move_files "bmp" "Images"
move_files "svg" "Images"
move_files "tiff" "Images"
move_files "webp" "Images"
move_files "ico" "Images"

# Organize documents
move_files "pdf" "Documents"
move_files "doc" "Documents"
move_files "docx" "Documents"
move_files "txt" "Documents"
move_files "odt" "Documents"
move_files "ppt" "Documents"
move_files "pptx" "Documents"
move_files "xls" "Documents"
move_files "xlsx" "Documents"
move_files "rtf" "Documents"
move_files "md" "Documents"
move_files "csv" "Documents"

# Organize videos
move_files "mp4" "Videos"
move_files "mkv" "Videos"
move_files "avi" "Videos"
move_files "mov" "Videos"
move_files "flv" "Videos"
move_files "wmv" "Videos"
move_files "webm" "Videos"

# Organize music/audio
move_files "mp3" "Music"
move_files "wav" "Music"
move_files "flac" "Music"
move_files "aac" "Music"
move_files "ogg" "Music"
move_files "m4a" "Music"
move_files "wma" "Music"

# Organize archives
move_files "zip" "Archives"
move_files "tar" "Archives"
move_files "gz" "Archives"
move_files "rar" "Archives"
move_files "bz2" "Archives"
move_files "7z" "Archives"

# Organize executables
move_files "sh" "Executables"
move_files "exe" "Executables"
move_files "bin" "Executables"
move_files "msi" "Executables"
move_files "apk" "Executables"
move_files "bat" "Executables"

# Organize code files
move_files "py" "Code"
move_files "js" "Code"
move_files "html" "Code"
move_files "css" "Code"
move_files "php" "Code"
move_files "java" "Code"
move_files "cpp" "Code"
move_files "c" "Code"
move_files "h" "Code"
move_files "cs" "Code"
move_files "rb" "Code"
move_files "swift" "Code"
move_files "go" "Code"
move_files "ts" "Code"
move_files "json" "Code"
move_files "xml" "Code"

# Organize fonts
move_files "ttf" "Fonts"
move_files "otf" "Fonts"
move_files "woff" "Fonts"
move_files "woff2" "Fonts"

# Organize CAD and 3D models
move_files "stl" "3D_Models"
move_files "obj" "3D_Models"
move_files "fbx" "3D_Models"
move_files "blend" "3D_Models"
move_files "dae" "3D_Models"

# Organize design files
move_files "psd" "Designs"
move_files "ai" "Designs"
move_files "xd" "Designs"
move_files "fig" "Designs"
move_files "sketch" "Designs"

# Organize disk images
move_files "iso" "Disk_Images"
move_files "img" "Disk_Images"
move_files "dmg" "Disk_Images"

# Organize torrents
move_files "torrent" "Torrents"

# Organize eBooks
move_files "epub" "eBooks"
move_files "mobi" "eBooks"
move_files "azw3" "eBooks"
move_files "cbz" "eBooks"
move_files "cbr" "eBooks"

# Organize spreadsheets
move_files "ods" "Spreadsheets"
move_files "xlsm" "Spreadsheets"

# Organize presentations
move_files "odp" "Presentations"
move_files "key" "Presentations"

# Organize databases
move_files "sql" "Databases"
move_files "db" "Databases"
move_files "sqlite" "Databases"
move_files "mdb" "Databases"

# Organize other files
move_files "log" "Other"
move_files "bak" "Other"
move_files "tmp" "Other"

echo "File organization complete!"
