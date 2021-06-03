#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  if (parseInt(process.argv[2]) > 0) {
    [...Array(parseInt(process.argv[2])).keys()].forEach(k => console.log('C is fun'));
  }
}
