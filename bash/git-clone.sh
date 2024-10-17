#! /bin/bash
# Auther: @codedsprit <roshan0x01@gmail.com>
#
# A simple script to clone a GitHub repository and remove its '.git' directory
read path
project="https://github.com/$path"
git clone $project
file=$(echo $path | sed 's/.*.\///')
rm -rf $file/.git
