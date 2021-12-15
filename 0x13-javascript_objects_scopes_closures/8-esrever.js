#!/usr/bin/node
exports.esrever = function (list) {
  let size = list.length;
  const newList = [];
  while (size-- > 0) {
    newList.push(list[size]);
  }
  return newList;
};
