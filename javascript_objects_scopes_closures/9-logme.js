#!/usr/bin/node
let currentNum = 0;

exports.logMe = function (item) {
  console.log(`${currentNum}: ${item}`);
  currentNum++;
};
