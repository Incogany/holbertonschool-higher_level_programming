#!/usr/bin/node
// script js
let i = 0;
exports.callMeMoby = function (x, theFunction) {
  while (i < x) {
    theFunction();
    i += 1;
  }
};
