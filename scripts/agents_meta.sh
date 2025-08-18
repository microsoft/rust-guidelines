#!/bin/bash

# Script to generate .meta files for all .md files in the agents directory
# Each .meta file contains size and token count information
# Excludes README.md files

set -euo pipefail

# Get the script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
AGENTS_DIR="$PROJECT_ROOT/src/agents"

# Check if agents directory exists
if [[ ! -d "$AGENTS_DIR" ]]; then
    echo "Error: $AGENTS_DIR directory not found"
    exit 1
fi

echo "Generating .meta files for markdown files in $AGENTS_DIR..."

# Counter for processed files
processed_count=0

# Find all .md files in agents directory, excluding READMEs
for md_file in "$AGENTS_DIR"/*.md; do
    # Check if file exists (glob expansion protection)
    if [[ ! -f "$md_file" ]]; then
        continue
    fi
    
    # Skip README files (case insensitive)
    basename_file=$(basename "$md_file")
    if [[ "${basename_file,,}" == "readme.md" ]]; then
        echo "  Skipping: $basename_file"
        continue
    fi
    
    # Generate .meta file path
    meta_file="${md_file%.*}.meta"
    
    # Get file size in bytes
    file_size_bytes=$(wc -c < "$md_file")
    
    # Format file size
    if [[ $file_size_bytes -lt 1024 ]]; then
        size_str="${file_size_bytes} bytes"
    elif [[ $file_size_bytes -lt $((1024 * 1024)) ]]; then
        file_size_kb=$((file_size_bytes / 1024))
        size_str="~${file_size_kb} kb"
    else
        file_size_mb=$((file_size_bytes / (1024 * 1024)))
        size_str="~${file_size_mb} MB"
    fi
    
    # Estimate tokens (roughly 4 characters per token for English text)
    estimated_tokens=$((file_size_bytes / 4))
    if [[ $estimated_tokens -lt 1000 ]]; then
        estimated_ktokens=0
    else
        estimated_ktokens=$((estimated_tokens / 1000))
    fi
    
    # Generate meta content
    meta_content="${size_str}, ~${estimated_ktokens}k tokens"
    
    # Write .meta file
    echo "$meta_content" > "$meta_file"
    
    echo "  $(basename "$md_file") -> $(basename "$meta_file") ($meta_content)"
    processed_count=$((processed_count + 1))
done

if [[ $processed_count -eq 0 ]]; then
    echo "No markdown files found to process (excluding READMEs)"
else
    echo "Successfully generated $processed_count .meta files"
fi