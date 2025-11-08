#!/bin/bash
# Usage: ./replace_placeholders.sh <directory_with_workflows>

WORKFLOW_DIR="$1"

# Replace placeholders in all YAML files in the workflows directory
for file in "$WORKFLOW_DIR"/*.yaml; do
    sed -i 's|PLACEHOLDER_FOR_PYTHON_VERSION|$3.11|g' "$file"
done
