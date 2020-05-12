#!/usr/bin/node
// script that display the status code of a GET request.

const number = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/' + number;
const request = require('request');
request(URL, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    console.log(info.title);
  }
});
