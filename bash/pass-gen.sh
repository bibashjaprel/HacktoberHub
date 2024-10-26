#!/bin/bash
# Author: @codedsprit <roshan0x01@gmail.com>
# Password generator with additional characters
# Set the length for the password, default to 25 if not provided

length=${1:-25}
< /dev/urandom tr -dc 'A-Za-z0-9_!@#$%^&*(){}[];:,.<>?123456789' | head -c "$length"; echo
