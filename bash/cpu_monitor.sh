#!/bin/bash

# Script to monitor CPU usage

echo "CPU Usage:"
mpstat | awk '$3 ~ /[0-9.]+/ { print 100 - $12"%"}'
