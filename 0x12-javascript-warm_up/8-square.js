#!/usr/bin/node
// script that prints a square

const value = parseInt(process.argv[2]);
let i = 0; let j = 0;

if (Number.isNaN(value)) {
  console.log('Missing size');
}
while (i < value) {
  while (j < value) {
    console.log('X'.repeat(value));
    j += 1;
  }
  i += 1;
}
