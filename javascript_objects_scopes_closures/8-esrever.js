#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];

  for (const item of list) {
    revList.unshift(item);
  }

  return revList;
};
