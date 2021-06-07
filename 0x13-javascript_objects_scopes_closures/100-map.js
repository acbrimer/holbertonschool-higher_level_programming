#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newList = list.map((v, ix) => v * ix);
console.log(newList);
