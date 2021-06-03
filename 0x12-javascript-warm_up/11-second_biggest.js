#!/usr/bin/node
const args = process.argv.slice(2, process.argv.length);
console.log(args.length > 1 ? args.sort((a, b) => a - b)[1] : 0);
