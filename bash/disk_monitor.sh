#!/bin/bash

# Script to monitor Disk space usage

echo "Disk Usage:"
df -h --total | grep 'total' | awk '{ print $3 "/" $2 " used (" $5 ")"}'
