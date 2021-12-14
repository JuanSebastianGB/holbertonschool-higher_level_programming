#!/usr/bin/node
exports.callMeMoby = (num, callback) => {
  for (let index = 0; index < num; index++) {
    callback();
  }
};
