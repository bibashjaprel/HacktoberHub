
#!/bin/bash
# Author: @codedsprit <roshan0x01@gmail.com>
#
# Yes, password generator 
length=${1:-25}
< /dev/urandom tr -dc 'A-Za-z0-9_@#$%^&*' | head -c "$length"; echo
