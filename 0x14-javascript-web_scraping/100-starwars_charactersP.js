#!/usr/bin/node
const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <Movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

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
    // Parse the response body
    const data = JSON.parse(body);
    const characters = data.characters;

    // Iterate through the characters and make a request to get each character's name
    characters.forEach((characterUrl) => {
      request(characterUrl, (err, res, characterBody) => {
        if (err) {
          console.error('Error:', err);
        } else if (res.statusCode !== 200) {
          console.error('Error: Received status code', res.statusCode);
        } else {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        }
      });
    });
  }
});

