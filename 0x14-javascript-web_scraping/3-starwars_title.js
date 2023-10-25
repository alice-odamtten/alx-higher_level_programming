#!/usr/bin/node
const args = process.argv;

const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${args[2]}`, (error, res, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
