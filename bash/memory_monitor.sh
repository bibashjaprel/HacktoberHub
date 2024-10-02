#!/bin/bash

# Script to monitor Memory usage

echo "Memory Usage:"
free -h | awk '/^Mem:/ { print $3 "/" $2 " used" }'
