#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Capture URL from command line argument
URL=$1

# Send GET request with curl and store response in a variable
response=$(curl -sI "$URL")

# Extract size of response body using wc
size=$(echo "$response" | awk '/Content-Length/ {print $2}')

# Display size of response body in bytes
echo "Size of response body: $size bytes
