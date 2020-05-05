#!/usr/bin/node
// script that prints add two numbers

const first = parseInt(process.argv[2]);

if (Number.isNaN(first) || first === 0 || first === 1) {
  console.log(parseInt('1'));
} else {
  console.log(factorial(first));
}
function factorial (n) {
  if (n > 1) {
    return n * factorial(n - 1);
  }
  return 1;
}
