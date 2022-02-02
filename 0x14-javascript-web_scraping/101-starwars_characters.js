#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (error, data, body) => {
  const initialindex = 0;
  if (error) { return error; }
  const characters = JSON.parse(body).characters;
  HandleCharacters(characters, initialindex);
});

const HandleCharacters = (characters, index) => {
  request(characters[index], function (error, data, body) {
    if (error) { return error; }
    console.log(JSON.parse(body).name);
    if (index + 1 < characters.length) {
      HandleCharacters(characters, index + 1);
    }
  });
};
