#!/bin/bash

echo "Enter a commit message:"
read COMMIT_MSG

git add .
git commit -m "$COMMIT_MSG"
git push

echo "Changes pushed to remote repository!"
