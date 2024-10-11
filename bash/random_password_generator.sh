#!/bin/bash
# It will generate random pasword based on the lemgth given
if [ -z "$1" ]; then
  echo "Usage: $0 <password-length>"
  exit 1
fi
password_length=$1
password=$(openssl rand -base64 48 | cut -c1-$password_length)
echo "Generated Password: $password"
