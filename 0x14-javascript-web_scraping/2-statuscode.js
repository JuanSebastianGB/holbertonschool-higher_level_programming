#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, data) => {
  console.log(err || `code: ${data.statusCode}`);
});
