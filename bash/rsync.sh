#!/bin/bash
# Author: @codedsprit <roshan0x01@gmail.com>

# Define source and destination directories
SOURCE="./A"
DESTINATION="./B"

# Ensure source and destination directories are provided
if [[ -z "$SOURCE" || -z "$DESTINATION" ]]; then
    echo "Error: Source or destination directory not specified."
    exit 1
fi

# Perform the synchronization
rsync -av --delete "$SOURCE/" "$DESTINATION/"

# Check if rsync was successful
if [[ $? -eq 0 ]]; then
    echo "Synchronization completed successfully."
else
    echo "Error: Synchronization failed."
    exit 1
fi
