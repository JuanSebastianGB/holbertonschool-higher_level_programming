#!/usr/bin/node
const input = process.argv;
const getFactorial = (input) => {
  input = parseInt(input);
  return input === 0 || isNaN(input) ? 1 : input * getFactorial(input - 1);
};
console.log(getFactorial(input[2]));
