#!/usr/bin/node
// script that display the status code of a GET request.

const URL = process.argv[2];
const request = require('request');
request.get(URL).on('response', function (response) {
  console.log('code: %d', response.statusCode);
});
