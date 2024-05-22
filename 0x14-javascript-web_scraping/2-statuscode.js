#!/usr/bin/node
const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

// Make a GET request to the provided URL
request(url, (error, response) => {
  if (error) {
    // Print the error object if an error occurred during the request
    console.error('Error:', error);
    process.exit(1);
  } else {
    // Print the status code
    console.log('code:', response.statusCode);
  }
});

