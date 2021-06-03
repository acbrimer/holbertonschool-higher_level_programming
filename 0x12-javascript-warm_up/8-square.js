#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  [...Array(parseInt(process.argv[2])).keys()].forEach(k => console.log('X'.repeat(parseInt(process.argv[2]))));
}
