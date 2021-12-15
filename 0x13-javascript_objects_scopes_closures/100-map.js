#!/usr/bin/node
const listGet = require('./100-data').list;
console.log(listGet);
console.log(listGet.map((a, index) => a * index));
