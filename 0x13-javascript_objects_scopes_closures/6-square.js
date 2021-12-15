#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    c = c === undefined ? 'X' : c;
    for (let index = 0; index < this.height; index++) console.log(c.repeat(this.width));
  }
};
