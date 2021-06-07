#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    [...Array(this.height)].forEach(r => console.log((c || 'X').repeat(this.width)));
  }
};
