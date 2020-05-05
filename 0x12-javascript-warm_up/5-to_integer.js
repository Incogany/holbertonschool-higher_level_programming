#!/usr/bin/node
// print process.argv
const val = parseInt(process.argv[2], 10);
if (Number.isNaN(val)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + val);
}
