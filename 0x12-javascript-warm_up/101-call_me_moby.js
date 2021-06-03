#!/usr/bin/node
module.exports = {
  callMeMoby: (x, theFunction) => x > 0 && [...Array(x).keys()].forEach(k => theFunction())
};
