#!/bin/sh
# Author: @codedsprit <roshan0x01@gmail.com>

# script to show ip the simple way

ip -br  addr show | awk '{print $3}'
