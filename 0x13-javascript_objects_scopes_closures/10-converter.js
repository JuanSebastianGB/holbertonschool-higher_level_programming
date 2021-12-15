#!/usr/bin/node
exports.converter = function (base) {
  return toReturn => toReturn.toString(base);
};
