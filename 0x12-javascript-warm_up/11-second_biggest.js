#!/usr/bin/node
const inputs = process.argv.map(Number);
if (inputs.length <= 3) {
  console.log(0);
} else {
  const result = inputs
    .slice(2)
    .sort((a, b) => a - b)
    .reverse()[1];
  console.log(result);
}
