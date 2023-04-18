#!/usr/bin/node
const dataList = require('./100-data').list;

const newList = dataList.map(function mul (num1, num2) {
  return num2 * num1;
});

console.log(dataList);
console.log(newList);
