#!/usr/bin/node
// print process.argv
let count = 0;
process.argv.forEach(() => {
  count += 1;
});
if (count === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
