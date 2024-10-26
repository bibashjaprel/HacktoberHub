
#!/bin/bash
# Author: @codedsprit <roshan0x01@gmail.com>
# Date: Oct 26 2024
# 
# script for simple todo list 
file="howdy.txt"
case $1 in
    add)
        echo "$2" >> "$file"
        ;;
    view)
        cat "$file"
        ;;
    remove)
        sed -i "/$2/d" "$file"
        ;;
    *)
        echo "Usage: $0 {add|view|remove} [task]"
        ;;
esac
