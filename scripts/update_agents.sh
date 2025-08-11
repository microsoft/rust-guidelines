#!/bin/bash

# Script to update agents/all.md with a concatenation of all guidelines
# This script inspects all folders under `guidelines` (except checklist)
# and includes each README.md followed by the M- guidelines in that folder

set -euo pipefail

# Get the script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SRC_DIR="$PROJECT_ROOT/src"
GUIDELINES_DIR="$SRC_DIR/guidelines"
OUTPUT_FILE="$SRC_DIR/agents/all.md"
META_FILE="$SRC_DIR/agents/all.meta"

# Create output directory if it doesn't exist
mkdir -p "$(dirname "$OUTPUT_FILE")"

# Start with header
cat > "$OUTPUT_FILE" << 'EOF'
# Single Page Guidelines

This file contains all guidelines concatenated for easy reference.

---

EOF

# Function to extract title from README.md (first # heading)
extract_title_from_readme() {
    local readme_file="$1"
    if [[ -f "$readme_file" ]]; then
        # Extract first line that starts with # 
        grep '^#' "$readme_file" | head -n1
    fi
}

# Function to process each guidelines subdirectory
process_guidelines_dir() {
    local dir="$1"
    local dir_name=$(basename "$dir")
    
    # Skip checklist directory as requested
    if [[ "$dir_name" == "checklist" ]]; then
        echo "Skipping checklist directory"
        return
    fi
    
    # Skip if not a directory
    if [[ ! -d "$dir" ]]; then
        return
    fi
    
    echo "Processing directory: $dir_name"
    
    # Add section header using the title from README.md
    if [[ -f "$dir/README.md" ]]; then
        local title=$(extract_title_from_readme "$dir/README.md")
        if [[ -n "$title" ]]; then
            echo "" >> "$OUTPUT_FILE"
            echo "$title" >> "$OUTPUT_FILE"
            echo "" >> "$OUTPUT_FILE"
        fi
    else
        echo "Warning: No README.md found in $dir"
        # Fallback section header
        echo "" >> "$OUTPUT_FILE"
        echo "# $(echo "$dir_name" | tr '[:lower:]' '[:upper:]') Guidelines" >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"
    fi
    
    # Include all M-*.md files in alphabetical order
    local m_files=()
    if ls "$dir"/M-*.md >/dev/null 2>&1; then
        for m_file in "$dir"/M-*.md; do
            if [[ -f "$m_file" ]]; then
                m_files+=("$m_file")
            fi
        done
        
        # Sort the array and clean up any carriage returns
        IFS=$'\n' m_files=($(printf '%s\n' "${m_files[@]}" | sort))
        unset IFS
        
        for m_file in "${m_files[@]}"; do
            # Strip any carriage returns from the filename
            m_file=$(echo "$m_file" | tr -d '\r')
            echo "Including: $(basename "$m_file")"
            echo "" >> "$OUTPUT_FILE"
            cat "$m_file" >> "$OUTPUT_FILE"
            echo "" >> "$OUTPUT_FILE"
        done
    else
        echo "No M-*.md files found in $dir"
    fi
    
    # Add separator between sections
    echo "" >> "$OUTPUT_FILE"
    echo "---" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
}

# Find all subdirectories in guidelines and process them
echo "Generating $OUTPUT_FILE..."

# Process directories in a consistent order (recursively)
for dir in "$GUIDELINES_DIR"/*/ "$GUIDELINES_DIR"/*/*/; do
    if [[ -d "$dir" ]]; then
        process_guidelines_dir "$dir"
    fi
done

# Generate metadata file with size and token estimates
if [[ -f "$OUTPUT_FILE" ]]; then
    # Get file size in KB
    file_size_bytes=$(wc -c < "$OUTPUT_FILE")
    file_size_kb=$((file_size_bytes / 1024))
    
    # Estimate tokens (roughly 4 characters per token for English text)
    estimated_tokens=$((file_size_bytes / 4))
    estimated_ktokens=$((estimated_tokens / 1000))
    
    # Format the output
    echo "~${file_size_kb} kb, ~${estimated_ktokens}k tokens" > "$META_FILE"
    
    echo "Successfully generated $OUTPUT_FILE (~${file_size_kb} kb, ~${estimated_ktokens}k tokens)"
    echo "Metadata saved to $META_FILE"
else
    echo "Error: Output file was not generated successfully"
    exit 1
fi

echo "File contains guidelines from the following directories:"
for dir in "$GUIDELINES_DIR"/*/ "$GUIDELINES_DIR"/*/*/; do
    if [[ -d "$dir" ]]; then
        # Get relative path from guidelines directory
        rel_path="${dir#$GUIDELINES_DIR/}"
        dir_name=$(basename "$dir")
        if [[ "$dir_name" != "checklist" ]]; then
            echo "  - $rel_path"
        fi
    fi
done