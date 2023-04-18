#!/usr/bin/node
const SquareExtends = require('./5-square');

class Square extends SquareExtends {
  charPrint (c) {
    const sign = c || 'X';

    for (let i = 0; i < this.height; i++) {
      console.log(sign.repeat(this.width));
    }
  }
}

module.exports = Square;
