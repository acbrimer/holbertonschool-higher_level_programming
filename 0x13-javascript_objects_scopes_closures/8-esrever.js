#!/usr/bin/node
exports.esrever = function (list) {
  const res = [];
  while (list.length) {
    res.push(list.pop());
  }
  return res;
};
