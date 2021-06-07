#!/usr/bin/node
const dict = require('./101-data').dict;
const newKeys = [...new Set(Object.values(dict).map(v => v))];
const newDict = Object.fromEntries(newKeys.map(k => [k, []]));
Object.keys(dict).forEach(k => newDict[dict[k]].push(k));
console.log(newDict);
