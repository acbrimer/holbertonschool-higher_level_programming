#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w && w > 0 && h && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    [...Array(this.height)].forEach(r => console.log('X'.repeat(this.width)));
  }
};
