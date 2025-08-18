#!/bin/bash

# Script to insert a build date into the top-level README.md file

# Get the current date in a desired format
DATE=$(date +"%Y-%m-%d")

# Replace the placeholder in your markdown file
sed -i "s/BUILD_DATE/$DATE/" src/guidelines/README.md
