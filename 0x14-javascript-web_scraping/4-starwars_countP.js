#!/usr/bin/node
const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = '18';

// Make a GET request to the provided API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    // Print the error object if an error occurred during the request
    console.error('Error:', error);
    process.exit(1);

  } else if (response.statusCode !== 200) {
    // Check for non-200 status code and handle it
    console.error('Error: Received status code', response.statusCode);
    process.exit(1);

  } else {
    // Parse the response body
    const data = JSON.parse(body);
    const films = data.results;
    let count = 0;

    // Iterate through the films and check if character ID 18 is present
    for (const film of films) {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count++;
      }
    }

    // Print the number of films where Wedge Antilles is present
    console.log(count);
  }
});

