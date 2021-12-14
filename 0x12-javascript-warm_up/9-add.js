#!/usr/bin/node
const inputs = process.argv;
const add = (inputs) => {
  if (inputs.length <= 3) {
    console.log(NaN);
    return;
  }
  return parseInt(inputs[2]) + parseInt(inputs[3]);
};
console.log(add(inputs));
