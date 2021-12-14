#!/usr/bin/node
const inputs = process.argv.map(Number);
if (inputs.length <= 3) {
  console.log(0);
} else {
  console.log(inputs.slice(2).sort().reverse()[1]);
}
