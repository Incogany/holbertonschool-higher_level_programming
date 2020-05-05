#!/usr/bin/node
// script that prints add two numbers
const myList = process.argv;
myList.splice(0, 2);
if (myList.length < 2) {
  console.log('0');
} else {
  myList.sort((a, b) => a - b);
  console.log(myList[myList.length - 2]);
}
