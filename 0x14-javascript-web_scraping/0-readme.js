#!/usr/bin/node
// script that reads and prints the content of a file.
/* const fs = require('fs');

try {
  const data = fs.readFileSync(process.argv[2], 'utf8');
  process.stdout.write(data);
} catch (err) {
  console.error(err);
}
*/
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
