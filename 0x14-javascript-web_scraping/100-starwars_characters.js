#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (err, data, body) => {
  if (err) { return err; }
  const characters = JSON.parse(body).characters;
  characters.map((character) => {
    request(character, (error, datacharacter, body) => {
      if (error) { return error; }
      console.log(JSON.parse(body).name);
    });
    return true;
  });
});
