#!/bin/bash

# Define the file containing repository URLs
REPOSITORY_FILE="repositories.txt"

# Check if the repository file exists
if [ ! -f "$REPOSITORY_FILE" ]; then
    echo "Error: File $REPOSITORY_FILE not found."
    exit 1
fi

# Read each line from the repository file
while IFS= read -r repo_url; do
    repo_name=$(basename "$repo_url" .git)
    repo_dir="$PWD/$repo_name"

    # Check if the repository directory already exists
    if [ -d "$repo_dir" ]; then
        echo "Updating $repo_name..."
        cd "$repo_dir" || exit
        git pull
        cd - || exit
    else
        echo "Cloning $repo_name..."
        git clone "$repo_url"
    fi

done < "$REPOSITORY_FILE"

echo "Repository update/clone completed."
