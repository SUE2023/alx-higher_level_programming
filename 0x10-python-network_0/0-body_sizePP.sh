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
size=$(echo "$response" | grep -iE 'Content-Length' | awk '{print $2}')

# Check if size is empty
if [ -z "$size" ]; then
    echo "Unable to determine the size of the response body."
else
    # Display size of response body in bytes
    echo "Size of response body: $size bytes"
fi
