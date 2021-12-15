#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
let value;
for (const key in dict) {
  value = dict[key];
  if (newDict[value] !== undefined) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
}
console.log(newDict);
