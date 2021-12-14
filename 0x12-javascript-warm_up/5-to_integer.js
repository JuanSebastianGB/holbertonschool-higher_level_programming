#!/usr/bin/node
const input = process.argv[2];
console.log(!isNaN(input) ? `My number: ${input}` : 'Not a number');
