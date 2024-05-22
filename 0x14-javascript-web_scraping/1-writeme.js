#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: ./script.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];

const stringToWrite = process.argv[3];

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    // Print the error object if an error occurred during writing
    console.error(err);
    process.exit(1);
  }
});

