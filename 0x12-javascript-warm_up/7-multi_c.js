#!/usr/bin/node
const input = process.argv[2];
const loop = (input) => {
  if (isNaN(input) || input === undefined) {
    console.log('Missing number of occurrences');
    return;
  }
  for (let index = 0; index < input; index++) {
    console.log('C is fun');
  }
};
loop(input);
