#!/bin/bash

# Location of the URL list
URL_LIST="/path/to/url-list.txt"

# Directory where files will be downloaded
DOWNLOAD_DIR="/path/to/download"

# Create the download directory if it doesn't exist
mkdir -p "$DOWNLOAD_DIR"

# Read each URL from the file and download it
while IFS= read -r URL; do
  if [[ ! -z "$URL" ]]; then
    echo "Downloading $URL..."
    wget -P "$DOWNLOAD_DIR" "$URL"
  fi
done < "$URL_LIST"

echo "All files downloaded to $DOWNLOAD_DIR."