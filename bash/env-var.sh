#!/bin/bash
# Author: @codedsprit <roshan0x01@gmail.com>
# Date: Oct 26 2024
#
# List env variable and grep specific.
#
if [ -z "$1" ]; then
    printenv
else
    printenv | grep "$1"
fi
