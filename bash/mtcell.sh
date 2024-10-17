#!/bin/sh
# Author: @codedsprit <roshan0x01@gmail.com>
#
# Mount android Phone in Linux 
mkdir -p ~/cell
echo -e DEVICES: "$(simple-mtpfs -l)"| dmenu # you can use fzf if you want
simple-mtpfs --device $(simple-mtpfs -l | awk '{printf "1\n"}') cell/
