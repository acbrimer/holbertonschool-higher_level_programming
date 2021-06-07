#!/usr/bin/node
const Square5 = require('./5-rectangle');

module.exports = class Square extends Square5 {
  charPrint (c) {
    [...Array(this.height)].forEach(r => console.log((c || 'X').repeat(this.width)));
  }
};
