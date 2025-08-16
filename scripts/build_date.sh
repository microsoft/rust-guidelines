#!/bin/bash

# Script to insert a build date into the SUMMARY.md file

# Get the current date in a desired format
DATE=$(date +"%Y-%m-%d %H:%M:%S")

# Replace the placeholder in your markdown file
sed -i "s/BUILT_ON_DATE/$DATE/" src/SUMMARY.md
