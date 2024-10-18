#!/bin/sh
# Author: @codedsprit <roshan0x01@gmail.com>

bat_dir=/sys/class/power_supply/BAT0

read -r capacity < "$bat_dir/capacity"
read -r status   < "$bat_dir/status"
if [[ $capacity -gt 85 ]]
then
echo -e "\e[36m  "[$capacity%]" "[$status]""
else

    echo -e "\e[31m  "[$capacity%]" "[$status]""
fi
