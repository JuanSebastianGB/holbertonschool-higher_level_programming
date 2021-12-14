#!/usr/bin/node
const input = process.argv;
const compute = (input) => {
  if (input === undefined || isNaN(input)) {
    console.log('Missing size');
    return;
  }
  let i = 0;
  while (i++ < input) {
    console.log('X'.repeat(input));
  }
};
compute(input[2]);
