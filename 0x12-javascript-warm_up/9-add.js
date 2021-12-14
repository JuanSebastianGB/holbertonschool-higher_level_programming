#!/usr/bin/node
const inputs = process.argv;
const add = (inputs) => {
  if (inputs.length <= 3 || isNaN(inputs[2]) || isNaN(inputs[3])) {
    return NaN;
  }
  return parseInt(inputs[2]) + parseInt(inputs[3]);
};
console.log(add(inputs));
