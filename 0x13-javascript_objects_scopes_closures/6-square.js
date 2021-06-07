#!/usr/bin/node
const Square = require('./5-rectangle');

module.exports = class Square extends Square {
  charPrint (c) {
    [...Array(this.height)].forEach(r => console.log((c || 'X').repeat(this.width)));
  }
};
