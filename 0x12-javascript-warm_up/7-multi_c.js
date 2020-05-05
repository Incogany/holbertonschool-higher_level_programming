#!/usr/bin/node
// script that prints 3 lines

const value = parseInt(process.argv[2]);
let i = 0;

if (Number.isNaN(value)) {
  console.log('Missing number of occurrences');
}
while (i < value) {
  console.log('C is fun');
  i += 1;
}
