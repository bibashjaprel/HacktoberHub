
#!/bin/bash
# Author: @codedsprit <roshan0x01@gmail.com>
#
# check argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

file="$1"

if [ ! -f "$file" ]; then
    echo "Error: File '$file' does not exist."
    exit 1
fi

# upload the file to 0x0.st
response=$(curl -F "file=@$file" https://0x0.st)

# check if the upload was successful or not.
if [ $? -eq 0 ]; then
    echo "File uploaded successfully!"
    echo "Uploaded file URL: $response"
else
    echo "Failed to upload file."
fi
