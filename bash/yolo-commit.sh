#!/bin/bash
# Author: @codedsprit <roshan0x01@gmail.com>

# Grabbing Random text from whatthecommit site 
commit=$(curl https://whatthecommit.com/index.txt)

git commit -m "$commit" 
git push origin main
