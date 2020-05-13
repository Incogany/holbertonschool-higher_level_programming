#!/usr/bin/node
// script that display the status code of a GET request.

const URL = process.argv[2];
const request = require('request');
request(URL, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const x in results) {
      const characters = results[x].characters;
      for (const y in characters) {
        if (characters[y].search('/18/') > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
