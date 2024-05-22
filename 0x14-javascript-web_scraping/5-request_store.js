#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: ./script.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the provided URL
request(url, (error, response, body) => {
  if (error) {
    // Print the error object if an error occurred during the request
    console.error('Error:', error);
    process.exit(1);

  } else if (response.statusCode !== 200) {
    // Check for non-200 status code and handle it
    console.error('Error: Received status code', response.statusCode);
    process.exit(1);

  } else {
    // Write the response body to the file in utf-8 encoding
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        // Print the error object if an error occurred during writing
        console.error('Error:', err);
        process.exit(1);
      }
    });
  }
});

