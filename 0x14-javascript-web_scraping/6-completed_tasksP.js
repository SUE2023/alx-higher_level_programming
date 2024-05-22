#!/usr/bin/node
const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

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
    const todos = JSON.parse(body);
    const completedTasks = {};
    // Iterate through the todos and count completed tasks by user ID
    todos.forEach(todo => {
      if (todo.completed) {
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 0;
        }
        completedTasks[todo.userId]++;
      }
    });

    // Print users with completed tasks
    for (const userId in completedTasks) {
      if (Object.prototype.hasOwnProperty.call(completedTasks, userId)) {
        console.log(`User ${userId}: ${completedTasks[userId]} completed tasks`);
      }
    }
  }
});

