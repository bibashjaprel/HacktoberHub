#!/bin/bash
# A simple hexdump like program written in pure bash
if [ $# -ne 1 ]; then 
    printf "Usage: %s <filename>\n " "$0"
    exit 1
fi

if [ ! -f "$1" ]; then 
  printf "Error: %s is not a file\n" "$1"
  exit 1
fi

od -A x -t x1z -v "$1"o | awk '{for(i=2; i<NF-1; i++) printf("%s ", $1); if(NF>2) printf("\n");}'
