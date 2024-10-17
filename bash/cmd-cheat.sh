#!/bin/bash
# Author: @codedsprit <roshan0x01@gmail.com>
#
# Define color variables
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
RESET='\033[0m'
 
# Define an array to hold the cheatsheet entries
entries=(
        "..   -> 'cd ..'"
        "...  -> 'cd ../../'"
        "bc   -> 'bc -ql'"
        "cat  ->  bat"
        "cp   -> 'cp -iv'"
        "gcl  -> 'git clone --depth=1 --filter=blob:none'"
        "ll   -> 'eza --icons  -T -L 2 -x'"
        "ls   -> 'eza --icons  -T -L 1 -x'"
        "v    -> nvim"
        "vi   -> 'vi -i NONE'"
        "vim  -> nvim"
        "wget -> 'wget --no-hsts'"
        "which-command -> whence"
)
 
# Create the alias with colored output
echo -e "${MAGENTA} ______________________________________________________________________${RESET}"
 
for entry in "${entries[@]}"; do
    cmd="${entry%%->*}"
    desc="${entry##*->}"
 
    # Calculate the required padding for command column
    padding=$(( 25 - ${#cmd} ))
    padding_spaces=$(printf '%*s' $padding)
 
    printf "${WHITE}|${RESET}${CYAN} %s${RESET}${YELLOW}->${RESET} ${GREEN}%-41s${RESET}${WHITE}|\n" "$cmd$padding_spaces" "$desc"
    (( count++ ))
    if [ $count -eq 4 ]; then
        echo -e "${WHITE}------------------------------------------------------------------------${RESET}"
    fi
 
done
 
echo -e "${MAGENTA}_______________________________________________________________________${RESET}"
 
