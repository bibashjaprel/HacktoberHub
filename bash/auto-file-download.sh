#!/bin/bash
# A simple bash script to download image files from given url target.

# Location of the URL list
URL_LIST="/home/sprit/hello/url.txt"
# Directory where files will be downloaded
DOWNLOAD_DIR="/home/sprit/hello"
# Create the download directory if it doesn't exist
mkdir -p "$DOWNLOAD_DIR"
# Read each URL from the file and download it
while IFS= read -r URL; do
  URL=$(echo "$URL" | xargs)

  if [ -n "$URL" ]; then
    FILENAME=$(basename "$URL")    
# skipping dublicate file to download.
    if [ -f "$DOWNLOAD_DIR/$FILENAME" ]; then
      echo "File '$FILENAME' already exists. Skipping download."
    else
      echo "Downloading $URL..."
      if wget -P "$DOWNLOAD_DIR" "$URL"; then
        echo "Successfully downloaded '$FILENAME'."
      else
        echo "Failed to download '$URL'."
      fi
    fi
  fi
done < "$URL_LIST"

echo "All downloads processed. Files saved to $DOWNLOAD_DIR."
