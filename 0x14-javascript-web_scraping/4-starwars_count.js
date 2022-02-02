#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

const FilterFunction = (data) => {
  const result = data.filter(characters => {
    return characters.includes('18');
  });
  return result.length;
};

request(url, (err, data, body) => {
  const result = JSON.parse(body).results;
  if (err) {
    console.log(err);
    return;
  }

  let count = 0;
  result.map(dictionary => {
    if (FilterFunction(dictionary.characters) > 0) { count++; }
    return count;
  });
  console.log(count);
});
