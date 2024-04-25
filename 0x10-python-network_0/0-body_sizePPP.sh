#!/bin/bash
# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Capture URL from command line argument
URL=$1

# Send GET request with curl and store response body in a variable
response_body=$(curl -s "$URL")

# Count the bytes of the response body
size=$(echo -n "$response_body" | wc -c)

# Display size of response body in bytes
echo "Size of response body: $size bytes"
