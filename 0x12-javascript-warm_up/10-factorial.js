#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1) {
    console.log(1);
  } else {
    console.log(isNaN([...Array(n).keys()].reverse().reduce((a, c) => a + a * c, 1)) ? 'Infinity' : [...Array(n).keys()].reverse().reduce((a, c) => a + a * parseFloat(c), parseFloat(1)));
  }
}
factorial(isNaN(parseInt(process.argv[2])) ? 1 : parseFloat(process.argv[2]));
