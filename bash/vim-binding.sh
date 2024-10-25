
#!/bin/bash
#Author: @codedsprit <roshan0x01@gmail.com>
clear

echo  "

\033[38;5;94m
      _       
 __ _(_)_ __  
 \ V / | '  \ 
  \_/|_|_|_|_|
           @codedsprit\033[0m

\033[1;33mModes:\033[0m
 Esc            - Normal mode
 i              - Insert before cursor
 a              - Append after cursor
 v              - Visual (select) mode

\033[1;33mNavigation:\033[0m
 h j k l        - Move left, down, up, right
 0              - Start of line
 $              - End of line
 w              - Next word
 b              - Previous word
 gg             - Start of file
 G              - End of file
 :N             - Go to line N (e.g., :5)

\033[1;33mEditing:\033[0m
 i              - Insert before cursor
 a              - Insert after cursor
 o              - New line below
 O              - New line above
 x              - Delete character
 dd             - Delete line
 yy             - Copy line
 p              - Paste after cursor
 r              - Replace character
 u              - Undo
 Ctrl + r       - Redo

\033[1;33mVisual Mode (Selecting Text):\033[0m
 v              - Select text
 V              - Select lines
 Ctrl + v       - Column select

\033[1;33mSearch:\033[0m
 /text          - Search 'text'
 n              - Next result
 N              - Previous result

\033[1;33mBinding for Replacement:\033[0m
 :%s/old/new/g  - Replace 'old' with 'new' in file

\033[1;33mSaving and Exiting:\033[0m
 :w             - Save
 :q             - Quit
 :wq or ZZ      - Save and quit
 :q!            - Quit without saving

==============================
       End of Cheat Sheet     
==============================
"
