#!/usr/bin/node
module.exports = {
  callMeMoby: (x, theFunction) => [...Array(x).keys()].forEach(k => theFunction())
};
