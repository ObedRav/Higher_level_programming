#!/usr/bin/node
if (!process.argv[3] || !process.argv[4]) {
  console.log(0);
}

const findSecond = (arr) => {
  const sortedArr = arr.sort();
  return sortedArr[sortedArr.length - 2];
};

const argvArr = process.argv.slice(2);

console.log(findSecond(argvArr));
