#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];

// Read the file content in utf-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    // Print the error object if an error occurred during reading
    console.error(err);
    process.exit(1);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
