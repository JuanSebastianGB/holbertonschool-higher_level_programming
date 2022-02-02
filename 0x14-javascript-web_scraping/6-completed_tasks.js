#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, data, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const content = JSON.parse(body);
  const userdict = {};
  content.map(dictionary => {
    if (dictionary.completed && userdict[dictionary.userId] === undefined) {
      userdict[dictionary.userId] = 1;
    } else if (dictionary.completed) {
      userdict[dictionary.userId] += 1;
    }
    return userdict;
  });
  console.log(userdict);
});
