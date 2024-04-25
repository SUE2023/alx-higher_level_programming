#!/bin/bash
# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
# Capture URL from command line argument
URL=$1

# Send DELETE request with curl and store response in a variable
response=$(curl -s -X DELETE "$URL")

# Display body of the response
echo "$response"
