#!/bin/bash
# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
# Capture URL from command line argument
URL=$1

# Send GET request with curl, include X-School-User-Id header, and store response in a variable
response=$(curl -s -H "X-School-User-Id: 98" "$URL")

# Display body of the response
echo "$response"
