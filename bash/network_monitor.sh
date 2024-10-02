#!/bin/bash

# Script to monitor Network activity

interface=$(ip route | grep '^default' | awk '{print $5}')
echo "Network usage on interface $interface:"
ifstat -i $interface 1 1 | tail -n 1
