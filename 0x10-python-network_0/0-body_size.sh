#!/bin/bash
# Send GET request with curl and store displays the body of the response
curl -s "$URL" | wc -c
