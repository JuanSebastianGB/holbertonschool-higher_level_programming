#!/usr/bin/node
const inputs = process.argv.map(Number);
console.log(inputs.slice(2).sort().reverse()[1]);
