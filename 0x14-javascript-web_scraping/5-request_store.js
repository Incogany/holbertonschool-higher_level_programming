#!/usr/bin/node
// script that display the status code of a GET request.

const fs = require('fs');
const request = require('request');
const URL = process.argv[2];
const file = process.argv[3];

request(URL, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    fs.writeFile(file, body, 'utf-8', function (err, data) {
      if (err) {
        return console.log(err);
      }
    });
  }
});
