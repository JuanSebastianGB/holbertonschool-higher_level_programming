#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];

request(url, (err, data, body) => {
  if (err) return;
  fs.writeFile(filename, body, (error, response) => { console.log(error); });
});
