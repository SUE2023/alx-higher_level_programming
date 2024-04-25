#!/bin/bash
# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
# Capture URL from command line argument
URL=$1

# Send OPTIONS request with curl and store response in a variable
response=$(curl -s -X OPTIONS -i "$URL")

# Extract allowed HTTP methods from response
allowed_methods=$(echo "$response" | awk '/Allow:/ {print $2}')

# Display allowed HTTP methods
echo "Allowed HTTP methods for $URL: $allowed_methods"
