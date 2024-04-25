#!/bin/bash
# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
# Capture URL from command line argument
URL=$1

# Send GET request with curl and store response in a variable
response=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

# Check if response status code is 200
if [ "$response" -eq 200 ]; then
    # Send GET request again and display only the body of the response
    curl -s "$URL"
else
    echo "Response status code: $response"
fi
